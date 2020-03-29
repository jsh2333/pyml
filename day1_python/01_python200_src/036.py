list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1, 2, 3, 4, 5], ['a', 'b', 'c']]
list1[0] = 6
print(list1)      # [6, 2, 3, 4, 5]가 출력됨
def myfunc():
   print('안녕하세요')
list4 = [1, 2, myfunc]
list4[2]()       # ‘안녕하세요’ 가 출력됨
