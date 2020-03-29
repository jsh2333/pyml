dict1 = {'a':1, 'b':2, 'c':3}
print(dict1['a'])     # 1이 출력됨
dict1['d'] = 4
print(dict1)        # {‘a’:1, ‘b’:2’, ‘c’:3, ‘d’:4}가 출력되나 순서가 틀릴 수 있음
dict1['b'] = 7
print(dict1)        # {‘a’:1, ‘b’:7’, ‘c’:3, ‘d’:4}가 출력되나 순서가 틀릴 수 있음
print(len(dict1))    # 4가 출력됨
