#-------------------------------------------------
# 파이썬 코딩 도장
# 파일 입출력 - 객체저장하기
# https://dojang.io/mod/page/view.php?id=2327
#-------------------------------------------------
# pickling: 객체-> 파일 저장
# unpickling: 객체<- 파일 읽기
import os
import pickle

print("cwd: " + os.getcwd()) 
 
name = 'abc'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

print("writing...") 
with open('file3.p', 'wb') as file:    # file.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)    
print("reading...")

with open('file3.p', 'rb') as file:    # file.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)    
