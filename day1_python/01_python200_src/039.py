def add_number(n1, n2):
   ret = n1+n2
   return ret

def add_txt(t1, t2):
   print(t1+t2)
 
ans = add_number(10, 15)
print(ans)                   # 25가 출력됨
text1 = '대한민국~'
text2 ='만세!!'
add_txt(text1, text2)         # ‘대한민국~만세!!’가 출력됨
