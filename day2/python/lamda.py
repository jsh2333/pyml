# 람다(Lambda)
# https://wikidocs.net/64
# lambda 인자 : 표현식

def hap(x, y):
   return x + y
   
hap(10, 20)


# lamda
(lambda x,y: x + y)(10, 20)



#---
# map(함수, 리스트)
# 리스트로부터 원소를 하나씩 꺼내서 함수를 적용
map(lambda x: x ** 2, range(5))           # 파이썬 2
# [0, 1, 4, 9, 16]  
list(map(lambda x: x ** 2, range(5)))     # 파이썬 2 및 파이썬 3
# [0, 1, 4, 9, 16]


# map
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
a
#[1, 2, 3, 4]


# reduce(함수, 순서형 자료)
# 순서형 자료(문자열, 리스트, 튜플)의 원소들을 누적해서 함수적용
from functools import reduce  
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
# 10
reduce(lambda x, y: y + x, 'abcde')
# 'edcba'


# filter(함수, 리스트)
#0부터 9까지의 리스트 중에서 5보다 작은 것만 돌려주는 예제
filter(lambda x: x < 5, range(10))       # 파이썬 2
#[0, 1, 2, 3, 4]  
list(filter(lambda x: x < 5, range(10))) # 파이썬 2 및 파이썬 3
#[0, 1, 2, 3, 4]

# 홀수만 돌려주는 filter
# 람다에서 0은 '거짓'이므로 버림
filter(lambda x: x % 2, range(10))        # 파이썬 2
# [1, 3, 5, 7, 9]  
list(filter(lambda x: x % 2, range(10)))  # 파이썬 2 및 파이썬 3
# [1, 3, 5, 7, 9]