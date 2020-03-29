#----------------------
# while 구문의 탈출
#----------------------

x = 1
total = 0
while 1:
    total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x = x + 1
