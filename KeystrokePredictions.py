import readchar
import time
import string
import os
import numpy as np
import pandas as pd
from sklearn import svm
from joblib import dump, load

class KeystrokePredictions:
    input_word = 'password'

    def learn(self):
        # First get the input
        c = ''
        name = ''
        print('Your name is: ', end='', flush=True)
        while True:
            c = readchar.readkey()
            print(f'{c}', end='', flush=True)
            if c == readchar.key.ENTER: break
            name += c

        print(f'\nSo your name is {name}')


        # Getting the number of input loops
        print(f'How many times do you want to input the word?')
        loops = 0
        i = 0
        while True:
            c = readchar.readkey()
            print(f'{c}', end='', flush=True)
            if c == readchar.key.ENTER:
                break
            try:
                loops = int(c) + i * 10 * loops
            except:
                continue
            i += 1
        print(f'You want to input {loops} number of times.')

        print(f'Press Enter to start (the input word is {self.input_word})')
        while True:
            c = readchar.readkey()
            print(f'{c}', end='', flush=True)
            if c == readchar.key.ENTER: break

        word = "" # Word which will be typed out
        c = ''    # Each character read in
        delta = np.zeros((loops, len(self.input_word))) # Empty list to hold time differences between each keystroke
        i = 0 # Do it with and index so a step backwards is possible if a mistake was made
        while i < loops:
            word = ""
            c = ''
            char_counter = 0
            while c != readchar.key.ENTER:
                if c == '':
                    print('', i+1, end=': ', flush=True)
                start_time = time.time()
                c = readchar.readkey()
                # decoded = c.decode('UTF-8')
                decoded = c
                if decoded in list(string.ascii_letters) and char_counter < len(self.input_word):
                    print(decoded, end='', flush=True)
                    delta[i, char_counter] = (time.time() - start_time)
                    word += decoded
                    char_counter += 1
            print('')
            if word != self.input_word:
                print("Spelling mistake")
                i -= 1
            i += 1


        # Create the pandas dataframe
        df = pd.DataFrame(delta, columns=[(str(i)+e) for i,e in enumerate('password')])
        df['name'] = name

        # If there is already a csv put all information below
        if os.path.exists('keystrokes.csv'):
            old_df = pd.read_csv('keystrokes.csv')
            new_df = pd.concat([old_df, df])
            new_df.to_csv('keystrokes.csv', encoding='utf-8', index=False)
        else:
            df.to_csv('keystrokes.csv', encoding='utf-8', index=False)

    def train(self):
        try:
            df = pd.read_csv('keystrokes.csv')
        except FileNotFoundError:
            print('keystrokes.csv could not be found')
            exit()

        y = df.pop('name').values
        X = df

        clf = svm.SVC(gamma='scale')
        try:
            clf.fit(X, y)
        except ValueError:
            print('There is only one name in the array. Quite boring to test for one person right?')
            return

        dump(clf, 'keystrokes_model.joblib')
        print("Model saved successfully")

    def predict(self):
        # Load the classifier model
        try:
            clf = load('keystrokes_model.joblib')
        except FileNotFoundError:
            print('keystrokes_model.joblib could not be found')
            exit()

        print(f'Press Enter to start (the input word is {self.input_word})')
        while True:
            c = readchar.readkey()
            print(f'{c}', end='', flush=True)
            if c == readchar.key.ENTER: break

        # Loop trough one word again and record the timing
        delta = np.zeros(len(self.input_word)) # Empty list to hold time differences between each keystroke
        while True:
            word = ""
            c = ''
            char_counter = 0
            while c != readchar.key.ENTER:
                start_time = time.time()
                c = readchar.readchar()
                decoded = c
                if decoded in list(string.ascii_letters) and char_counter < len(self.input_word):
                    print(decoded, end='', flush=True)
                    delta[char_counter] = (time.time() - start_time)
                    word += decoded
                    char_counter += 1
            print('')
            if word == self.input_word:
                break
            print('Spelling mistake')

        delta = delta.reshape(1, -1)
        df = pd.DataFrame(delta)
        # If word was correct reshape the delta and predict the correct value
        print('Probably {} typed {}'.format(
            clf.predict(df)[0],
            self.input_word))

