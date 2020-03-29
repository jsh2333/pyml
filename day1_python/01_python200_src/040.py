def add_txt(t1, t2='파이썬'):
   print(t1+' : ' +t2)
   
add_txt('베스트')                   # ‘베스트 : 파이썬’이 출력됨
add_txt(t2='대한민국', t1='1등')    # ‘1등 : 대한민국’이 출력됨

def func1(*args):
   print(args)

def func2(width, height, **kwargs):
   print(kwargs)

func1()                          # 빈 튜플 ( ) 이 출력됨
func1(3, 5, 1, 5)                  # (3, 5, 1, 5)가 출력됨
func2(10, 20)                          # 빈 사전 { }이 출력됨
func2(10, 20, depth=50, color='blue')  #{‘depth’:50, ‘color’:’blue’} 이 출력됨
