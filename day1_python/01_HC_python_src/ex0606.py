# 코드 6-6 count가 2일 때 넘어가는 코드
count = 0
while count < 3:
    count = count + 1
    if count == 2:
        continue
    print(count)
