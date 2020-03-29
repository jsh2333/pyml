h1 = hex(97)       # h1은 문자열 ‘0x61’
h2 = hex(98)       # h2는 문자열 ‘0x62’
ret1 = h1 +h2      
print(ret1)          # ‘0x610x62’ 가 출력됨
a = int(h1, 16)
b = int(h2, 16)
ret2 = a + b       # ret2는 10진수 195가 됨
print(hex(ret2))     # ‘0xc3’ 가 출력됨
