from zipfile import *

def compressZip(zipname, filename):
    print('[%s] -> [%s] 압축...' %(filename, zipname))
    with ZipFile(zipname, 'w') as ziph:
        ziph.write(filename)
        
    print('압축이 끝났습니다.')
    
filename = 'mydata.txt'
zipname = filename + '.zip'
compressZip(zipname, filename)
