def countWord(filename, word):
   with open(filename, 'r') as f:
      text = f.read()
      text = text.lower()
      pos = text.find(word)
      count = 0
      while pos != -1:
         count += 1
         pos = text.find(word, pos+1)
   return count

word = input('mydata.txt에서 개수를 구할 단어를 입력하세요: ')
word = word.lower()
ret = countWord('mydata.txt', word)
print('[%s]의 개수: %d' %(word, ret))
