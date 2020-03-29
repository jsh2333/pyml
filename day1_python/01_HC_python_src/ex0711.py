# 코드 7-11 라면 주문을 추가/수정/취소하는 코드
order = {'스페이드1': '비빔라면', '다이아2': '매운라면'}
print(order)
order['클로버3'] = '카레라면'
print(order)
order['다이아2'] = '짜장라면'
print(order)
del order['스페이드1']
print(order)
