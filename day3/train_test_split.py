import numpy as np
from sklearn.model_selection import train_test_split

X = [[0,1],[2,3],[4,5],[6,7],[8,9]]
Y = [0,1,2,3,4]

# 데이터(X)만 넣었을 경우
X_train, X_test = train_test_split(X, test_size=0.2, random_state=123)
# X_train : [[0,1],[6,7],[8,9],[2,3]]
# X_test : [[4,5]]

# 데이터(X)와 레이블(Y)을 넣었을 경우
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=321)
# X_train : [[4,5],[0,1],[6,7]]
# Y_train : [2,0,3]
# X_test : [[2,3],[8,9]]
# Y_test : [1,4]
