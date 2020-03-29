class MyClass:    
    def __del__(self):
       print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')

obj = MyClass()
del obj         # ‘MyClass 인스턴스 객체가 메모리에서 제거됩니다’가 출력됨
