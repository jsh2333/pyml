# classification_report


# confusion_matrix(y_true, y_pred)
# accuracy_score(y_true, y_pred)
# precision_score(y_true, y_pred)
# recall_score(y_true, y_pred)
# fbeta_score(y_true, y_pred, beta)
# f1_score(y_true, y_pred)
# classfication_report(y_true, y_pred)
# roc_curve
# auc

import pandas as pd
import numpy as np
# import sklearn
# print('sklearn: %s' % sklearn.__version__)

from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import confusion_matrix

# create and configure model



X, y = make_classification(n_samples=16, n_features=2,
                           n_informative=2, n_redundant=0,
                           random_state=0)

# model = LogisticRegression().fit(X, y)
model = LogisticRegression(solver='liblinear').fit(X, y)
# model = LogisticRegression(solver='lbfgs').fit(X, y)
y_hat = model.predict(X)
f_value = model.decision_function(X)

df = pd.DataFrame(np.vstack([f_value, y_hat, y]).T, columns=["f", "y_hat", "y"])
df.sort_values("f", ascending=False).reset_index(drop=True)

print(df)

matrix = confusion_matrix(y, y_hat, labels=[1, 0])
print('confusion matrix: ')
print(matrix)

recall = 6 / (6 + 2)
fallout = 1 / (1 + 7)
print("recall =", recall)
print("fallout =", fallout)

