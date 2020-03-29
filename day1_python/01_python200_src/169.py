t1 = input('찾을 단어를 입력하세요: ')
t2 = input('변경할 단어를 입력하세요: ')

with open('mydata.txt', 'r') as f:
    with open('mydata2.txt', 'w') as h:
        text = f.read()
        text = text.replace(t1, t2)
        h.write(text)
        
print('[%s]를 [%s]로 변경하였습니다.' %(t1, t2))
