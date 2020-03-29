from datetime import datetime

start = datetime.now()
print('1에서 백만까지 더합니다.')
ret = 0
for i in range(1000000):
   ret += i
print('1에서 백만까지 더한 결과: %d' %ret)
end = datetime.now()
elapsed = end - start
print('총 계산 시간: ', end='');print(elapsed)
elapsed_ms = int(elapsed.total_seconds()*1000)
print('총 계산 시간: %dms' %elapsed_ms)
