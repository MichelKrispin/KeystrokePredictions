#!/usr/bin/env python3
from KeystrokePredictions import KeystrokePredictions

if __name__ == '__main__':
    k = KeystrokePredictions()
    
    print('Keystroke Predictions for the word "password"\n'
          '  learn   - For new or additional user input\n'
          '  train   - For training the machine learning model with all input\n'
          '  predict - For prediction of a user\n'
          '  quit    - Quit the application')

    while True:
        msg = input('>> ')
        if msg == 'exit' or msg == 'quit': break
        if msg == 'learn':
            k.learn()
        elif msg == 'train':
            k.train()
        elif msg == 'predict':
            k.predict()

