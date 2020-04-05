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

#----------------------------------
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

X, y = make_classification(n_samples=1000, weights=[0.95, 0.05], random_state=5)

model1 = LogisticRegression().fit(X, y)
y_hat1 = model1.predict(X)

model2 = SVC(gamma=0.0001, C=3000, probability=True).fit(X, y)
y_hat2 = model2.predict(X)


from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_hat1))

print(confusion_matrix(y, y_hat2))

# 두 모형은 분류결과표로 봤을 때는 성능이 같다

from sklearn.metrics import classification_report
print(classification_report(y, model1.predict(X)))
print(classification_report(y, model2.predict(X)))


# ROC curve 
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve
fpr1, tpr1, thresholds1 = roc_curve(y, model1.decision_function(X))
fpr2, tpr2, thresholds1 = roc_curve(y, model2.decision_function(X))

plt.plot(fpr1, tpr1, 'o-', ms=2, label="Logistic Regression")
plt.plot(fpr2, tpr2, 'o-', ms=2, label="Kernel SVM")
plt.legend()
plt.plot([0, 1], [0, 1], 'k--', label="random guess")
plt.xlabel('위양성률(Fall-Out)')
plt.ylabel('재현률(Recall)')
plt.title('ROC 커브')
plt.show()

#--------------------------------------
# AUC curve
from sklearn.metrics import auc
print('auc(model1):')
auc1 = auc(fpr1, tpr1)
print(auc1)
print('auc(model2):')
auc2 = auc(fpr2, tpr2)
print(auc2)
