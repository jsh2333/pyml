count = 1
data = []
print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')
while True:
   text = input('[%d] 파일에 저장할 내용을 입력하세요: ' %count)
   if text == '':
      break
   data.append(text+'\n')
   count += 1

f = open('mydata.txt', 'w')
f.writelines(data)
f.close()
