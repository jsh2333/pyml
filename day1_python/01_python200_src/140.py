text = input('파일에 저장할 내용을 입력하세요: ')
f = open('mydata.txt', 'w')
f.write(text)
f.close()
