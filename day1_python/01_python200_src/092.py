txt = 'A lot of things occur each day, every day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
print(offset1)   # 22가 출력됨
print(offset2)   # 27이 출력됨
print(offset3)   # 38이 출력됨
