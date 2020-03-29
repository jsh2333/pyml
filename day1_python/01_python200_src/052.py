class MyClass:    
    def __init__(self):
       self.var = '안녕하세요!'
       print('MyClass 인스턴스 객체가 생성되었습니다')

obj = MyClass()   # ‘MyClass 인스턴스 객체가 생성되었습니다’가 출력됨
print(obj.var)      # ‘안녕하세요’가 출력됨
