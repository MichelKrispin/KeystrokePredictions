import readchar
import time
import string
import numpy as np
import pandas as pd
import os


input_word = "password"

# First get the input
name = input("Your name is: ")
try:
    loops = int(input("Number of loops: "))
except ValueError:
    print("Please input a valid number")
    exit()

input("Press Enter to start (the input word is {})".format(input_word))

word = "" # Word which will be typed out
c = ''    # Each character read in
delta = np.zeros((loops, len(input_word))) # Empty list to hold time differences between each keystroke
i = 0 # Do it with and index so a step backwards is possible if a mistake was made
while i < loops:
    word = ""
    c = ''
    char_counter = 0
    # while c is not b'\x1b': # The escape character
    while c is not b'\r': # The enter character on windows
        if c == '':
            print('', i+1, end=': ', flush=True)
        start_time = time.time()
        c = readchar.readchar()
        decoded = c.decode('UTF-8')
        if decoded in list(string.ascii_letters) and char_counter < len(input_word):
            print(decoded, end='', flush=True)
            delta[i, char_counter] = (time.time() - start_time)
            word += decoded
            char_counter += 1
    print('')
    if word != input_word:
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
print(df)

