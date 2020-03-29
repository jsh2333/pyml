#-------------------------------------------------
# 파이썬 코딩 도장
# 파일 입출력 - 문자열 처리
# https://dojang.io/mod/page/view.php?id=2325
#-------------------------------------------------

# 파일객체 = open(파일이름, 파일모드)
# 파일객체.write('문자열')
# 파일객체.close()

#writing...
print("writing...")
file = open('file1.txt', 'w')     # file.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!')      # 파일에 문자열 저장
for i in range(3):
  file.write('Hello, world! {0}\n'.format(i))      # 파일에 문자열 저장
file.close()                     # 파일 객체 닫기

# reading...
print("reading...")
file = open('file1.txt', 'r')    # file.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()                     # 파일 객체 닫기


# reading...
print("reading...")
with open('file1.txt', 'r') as file:    # file.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력