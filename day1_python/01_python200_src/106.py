listdata = list(range(5))
ret1 = reversed(listdata)
print('원본 리스트 ', end='');print(listdata);
print('역순 리스트 ', end='');print(list(ret1))

ret2 = listdata[::-1]
print('슬라이싱 이용 ', end='');print(ret2)
