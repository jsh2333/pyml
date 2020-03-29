url = 'http://www.naver.com/news/today=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선'

ret1 = url.split('/')
print(ret1)

ret2 = log.split()
for data in ret2:
   d1, d2 = data.split(':')
   print('%s -> %s' %(d1, d2))
