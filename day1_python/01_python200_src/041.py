param = 10
strdata = '전역변수'

def func1():
   strdata = '지역변수'
   print(strdata)
   
def func2(param):
   param = 1
   
def func3():
   global param
   param = 50
   
func1()                  # ‘지역변수’가 출력됨
print(strdata)           # ‘전역변수’가 출력됨
print(param)             # 10이 출력됨
func2(param)
print(param)             # 10이 출력됨
func3()
print(param)             # 50이 출력됨
