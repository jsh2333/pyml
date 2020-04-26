#pip install glob3
# 파일들의 목록을 뽑을 때 사용
import glob
glob.glob('*.*')
glob.glob('*.py')
# ['LICENSE.txt', 'NEWS.txt', 'readme.txt']
exit()

import glob
for filename in glob.glob('*.jpg'):
    print(filename)

# 현재 디렉토리 내의 모든 파일
# import glob
# for filename in glob.iglob('**/*.jpg', recursive=True):
#     print(filename)    