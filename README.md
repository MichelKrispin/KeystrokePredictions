# KeystrokePredictions
This is a student project. It is neither complete nor very stable.

In one sentence this project can:
Read text input ('password') from different persons and then learn from that input to predict who typed this word based on the timing between each keystroke.

## How to run
First of all you will need some dependencies so create a venv. (All commands below are for unix systems)
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./Main.py
```

More than one person should type in multiple times the word 'password'. Otherwise the prediction is kind of useless...

With `learn` the user types in the word and writes it to a .csv table.
With `train` the user trains a machine learning model from that .csv table.
With `predict` the user uses the machine learning model to try to predict a newly typed word.
