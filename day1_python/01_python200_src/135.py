add = lambda x, y: x+y
ret = add(1, 3)
print(ret)    # 4가 출력됨

funcs = [lambda x: x+'.pptx', lambda x: x+'.docx']
ret1 = funcs[0]('Intro')
ret2 = funcs[1]('Report')
print(ret1)   # intro.pptx가 출력됨
print(ret2)   # Report.docx가 출력됨

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115,
          'Bob':5887, 'Kelly':7855}
ret3 = sorted(names.items(), key=lambda x: x[0])
print(ret3)
