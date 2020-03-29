# 코드 7-9 딕셔너리의 값에 접근하는 코드
clover = {'나이': 27, '직업': '병사', '번호': 9}
print(clover['번호'])
clover['번호'] = 6
print(clover['번호'])
print(clover.get('번호'))
