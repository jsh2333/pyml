num = input('아무 숫자를 입력하세요: ')

if num.isdigit():
   num = num[::-1]
   ret = ''
   for i, c in enumerate(num):
      i += 1
      if i != len(num) and i%3 == 0:
         ret += (c + ',')
      else:
         ret += c
   ret = ret[::-1]
   print(ret)
else:
   print('입력한 내용 [%s]: 숫자가 아닙니다.' %num)
