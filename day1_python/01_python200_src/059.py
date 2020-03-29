import time
count = 1
try:
   while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:   # Ctrl-C가 입력되면 발생하는 오류
   print('사용자에 의해 프로그램이 중단되었습니다.')
