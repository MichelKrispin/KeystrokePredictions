import pandas as pd
from sklearn import svm
import readchar
import time
import string
import numpy as np
from joblib import load

input_word = "password"

# Load the classifier model
try:
    clf = load('keystrokes_model.joblib')
except FileNotFoundError:
    print('keystrokes_model.joblib could not be found')
    exit()

input("Press Enter to start (the input word is {})".format(input_word))

# Loop trough one word again and record the timing
delta = np.zeros(len(input_word)) # Empty list to hold time differences between each keystroke
while True:
    word = ""
    c = ''
    char_counter = 0
    while c is not b'\r': # The enter character on windows
        start_time = time.time()
        c = readchar.readchar()
        decoded = c.decode('UTF-8')
        if decoded in list(string.ascii_letters) and char_counter < len(input_word):
            print(decoded, end='', flush=True)
            delta[char_counter] = (time.time() - start_time)
            word += decoded
            char_counter += 1
    print('')
    if word == input_word:
        break
    print('Spelling mistake')

delta = delta.reshape(1, -1)
df = pd.DataFrame(delta)
# If word was correct reshape the delta and predict the correct value
print('Probably {} typed {}'.format(
    clf.predict(df)[0],
    input_word))

