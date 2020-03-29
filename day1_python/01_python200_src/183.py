from os.path import exists

def getTop10BabyName(year):
    nameF = {}    
    nameM = {}
    
    filename = 'names/yob%s.txt' %year
    if not exists(filename):
        print('[%s] 파일이 존재하지 않습니다.' %filename)
        return None
    
    with open(filename, 'r') as f:
        data = f.readlines()
        for d in data:
            if d[-1] == '\n':
                d = d[:-1]

            tmp = d.split(',')
            name = tmp[0]
            sex = tmp[1]
            birth = tmp[2]

            if sex == 'F':
                ret = nameF
            else:
                ret = nameM
            
            if name in ret:
                ret[name] += int(birth)
            else:
                ret[name] = int(birth)

    retF = sorted(nameF.items(), key=lambda x:x[1], reverse=True)
    retM = sorted(nameM.items(), key=lambda x:x[1], reverse=True)
    
    for i, name in enumerate(retF):
        if i > 9:
            break            
        print('TOP_%d 여자아기이름: %s' %(i+1, name))
        
    for i, name in enumerate(retM):
        if i > 9:
            break            
        print('TOP_%d 남자아기이름: %s' %(i+1, name))

y = input('인기순 상위10개 이름을 알고 싶은 출생년도를 입력하세요(예:2001): ')
getTop10BabyName(y)
