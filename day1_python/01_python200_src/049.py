class MyClass:
   var = '안녕하세요'
   def sayHello(self):
      print(self.var)

obj = MyClass()    # MyClass 인스턴스 객체 생성
print(obj.var)     # ‘안녕하세요’가 출력됨
obj.sayHello()     # ‘안녕하세요’가 출력됨
