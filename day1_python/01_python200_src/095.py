txt = 'My password is 1234'
ret1 = txt.replace('1', '0')
ret2 = txt.replace('1', 'python')
print(ret1)   # ‘My Password is 0234’가 출력됨
print(ret2)   # ‘My Password is python234’가 출력됨

txt = '매일 많은 일들이 일어납니다.'
ret3 = txt.replace('매일', '항상')  
ret4 = ret3.replace('일', '사건')
print(ret3)   # ‘항상 많은 일들이 일어납니다.’가 출력됨
print(ret4)   # ‘항상 많은 사건들이 사건어납니다.’가 출력됨
