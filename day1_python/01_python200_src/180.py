from random import shuffle

male = ['슈퍼맨', '심봉사', '로미오', '이몽룡', '마루치']
female = ['원더우먼', '뺑덕', '줄리엣', '성춘향', '아라치']
shuffle(male)
shuffle(female)
couples = zip(male, female)

for i, couple in enumerate(couples):
   print('커플%d: [%s]-[%s]' %(i+1, couple[0], couple[1]))
