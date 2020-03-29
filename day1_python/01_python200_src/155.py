import os
from os.path import exists

dir_name = input('새로 생성할 디렉터리 이름을 입력하세요: ')
if not exists(dir_name):
   os.mkdir(dir_name)
   print('[%s] 디렉터리를 생성했습니다.' %dir_name)
else:
   print('[%s]은(는) 이미 존재합니다.' %dir_name)
