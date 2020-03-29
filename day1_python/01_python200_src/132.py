ch = input('문자를 1개 입력하세요: ')
if len(ch) != 0:
   ch = ch[0]
   chv = ord(ch)
   print('문자: %s \t코드값: %d [%s]' %(ch, chv, hex(chv)))
