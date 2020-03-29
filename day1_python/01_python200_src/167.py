with open('mydata.txt', 'r') as f:
   data = f.read()
   tmp = data.split()
   print('단어수: [%d]' %len(tmp))
