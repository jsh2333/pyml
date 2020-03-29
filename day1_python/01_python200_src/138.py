f = open('stockcode.txt', 'r')
line_num = 1
line = f.readline()
while line:
   print('%d %s' %(line_num, line), end='')
   line = f.readline()
   line_num += 1
f.close()
