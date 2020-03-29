class MyClass:    
    var = '안녕하세요!!'        
    def sayHello(self):
        param1 = '안녕'
        self.param2 = '하이'
        print(param1)        # ‘안녕’이 출력됨
        print(self.var)         # ‘안녕하세요’가 출력됨
      
obj = MyClass()
print(obj.var)                # ‘안녕하세요’가 출력됨
obj.sayHello()
#obj.param1
