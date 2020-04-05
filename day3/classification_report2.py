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



from sklearn.metrics import confusion_matrix

# 분류결과표(Confusion Matrix)
y_true = [1, 0, 1, 1, 0, 1]
y_pred = [0, 0, 1, 1, 0, 1]
confusion_matrix(y_true, y_pred)

result = confusion_matrix(y_true, y_pred)

print(result)

# labels 인수를 사용하면 순서를 사용자가 바꿀 수 있다.
result = confusion_matrix(y_true, y_pred, labels=[1, 0])

print(result)