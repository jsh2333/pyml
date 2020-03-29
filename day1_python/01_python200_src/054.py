class Add:    
   def add(self, n1, n2):
      return n1+n2

class Calculator(Add):
   def sub(self, n1, n2):
      return n1-n2

obj = Calculator()
print(obj.add(1, 2))   # 3이 출력됨
print(obj.sub(1, 2))   # -1이 출력됨
