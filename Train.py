import pandas as pd
from sklearn import svm
from sklearn import preprocessing
from joblib import dump

try:
    df = pd.read_csv('keystrokes.csv')
except FileNotFoundError:
    print('keystrokes.csv could not be found')
    exit()

y = df.pop('name').values
X = df
# X_scaled = preprocessing.scale(X)

clf = svm.SVC(gamma='scale')
# clf.fit(X_scaled, y)
clf.fit(X, y)

dump(clf, 'keystrokes_model.joblib')
print("Model saved successfully")
