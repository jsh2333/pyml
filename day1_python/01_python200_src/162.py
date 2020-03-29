text = input('문장을 입력하세요: ')

ret = ''
for i in range(len(text)):
    if i != len(text)-1:
        ret += text[i+1]
    else:
        ret += text[0]
        
print(ret)
