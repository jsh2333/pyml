import os
from sklearn import svm, metrics
import random, re
os.getcwd()
# 붓꽃의 CSV 데이터 읽어 들이기 --- (※1)
csv = []
with open('./day2/iris.csv', 'r', encoding='utf-8') as fp:
    # 한 줄씩 읽어 들이기
    for line in fp:
        line = line.strip()    # 줄바꿈 제거
        cols = line.split(',') # 쉼표로 자르기
        # 문자열 데이터를 숫자로 변환하기
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        # print(fn)
        # print(cols)
        cols = list(map(fn, cols))
        # print(cols)
        csv.append(cols)
# exit()            
# print(csv)
# print(csv[0])
    
# 가장 앞 줄의 헤더 제거
del csv[0]
# 데이터 셔플하기(섞기) --- (※2)
random.shuffle(csv)
# 학습 전용 데이터와 테스트 전용 데이터 분할하기(2:1 비율) --- (※3)
total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data  = csv[i][0:4] # 붓꽃구분 머신러닝 데이타
    label = csv[i][4] # 붓꽃구분 정답
    print(data)
    print(label)
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)
        
# 데이터를 학습시키고 예측하기 --- (※4)
clf = svm.SVC()
# print(clf)
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기 --- (※5)
ac_score = metrics.accuracy_score(test_label, pre) # 정답, 예측
# print(test_label)
# print(pre)
print("정답률 =", ac_score)