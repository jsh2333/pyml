import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

import glob, os.path, re, json
# print('cwd: '+ os.getcwd())
os.chdir('./day3')
# 데이터 읽어 들이기--- (※1)
mr = pd.read_csv("mushroom.csv", header=None)

# df_mr = pd.DataFrame(mr)
# print(df_mr.head())
# exit() 
#----------------------------------

# 데이터 내부의 기호를 숫자로 변환하기--- (※2)
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.ix[0])
    row_data = []
    for v in row.ix[1:]:
        row_data.append(ord(v))
    data.append(row_data)

# print(data)
# print(row_data)
# exit() 
#----------------------------------

# 학습 전용과 테스트 전용 데이터로 나누기 --- (※3)
data_train, data_test, label_train, label_test = \
    train_test_split(data, label)

# print('train: ')
# print(len(data_train))
# print(label_train)
# print(len(label_train))
# print('test: ')
# print(len(data_test))
# print(label_test)
# print(len(label_test))
# exit() 
#----------------------------------
# 데이터 학습시키기 --- (※4)
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

# 데이터 예측하기 --- (※5)
predict = clf.predict(data_test)

# 결과 테스트하기 --- (※6)
ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)