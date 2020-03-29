#-------------------------------------------------
# 파이썬 코딩 도장
# 파일 입출력 - 여러줄의 문자열 처리
# https://dojang.io/mod/page/view.php?id=2326
#-------------------------------------------------
import os

print("cwd: " + os.getcwd()) 

# writing
with open('file2.txt', 'w') as file:    # file.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

lines = ['안녕하세요.\n', 'Hello\n', 'python\n']
 
with open('file2.txt', 'w') as file:    # file.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)

# reading
with open('file2.txt', 'r') as file:    # file.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)


with open('file2.txt', 'r') as file:    # file.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력


with open('file2.txt', 'r') as file:    # file.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

