import pandas as pd
from sklearn import svm
from joblib import dump

try:
    df = pd.read_csv('keystrokes.csv')
except FileNotFoundError:
    print('keystrokes.csv could not be found')
    exit()

y = df.pop('name').values
X = df

clf = svm.SVC(gamma='scale')
clf.fit(X, y)

dump(clf, 'keystrokes_model.joblib')
print("Model saved successfully")
