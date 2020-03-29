def getPrime(x):
   for i in range(2, x-1):
      if x%i == 0:
         break
   else:
      return x

listdata = [117, 119, 1113, 11113, 11119]
ret = filter(getPrime, listdata)
print(list(ret))            # [11113, 11119] 가 출력됨
