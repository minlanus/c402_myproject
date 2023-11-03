# test.py

import svc_param_selection
from sklearn.metrics import classification_report

train = svc_param_selection.test
clf = svc_param_selection.clf
pd = svc_param_selection.pd

X_test = train[['3P', 'BLK']]
y_test = train[['Pos']]

y_true, y_pred = y_test, clf.predict(X_test)

print(classification_report(y_true, y_pred))

comparison = pd.DataFrame({'prediction': y_pred,
                           'ground_truth': y_true.values.ravel()})

print(comparison)