import sys
import os
import requests

 
resp = requests.get( 'http://daum.net' )
# resp.raise_for_status()
html=''
print("cwd: " + os.getcwd()) 
if (resp.status_code == requests.codes.ok):
    html = resp.text.encode('utf-8')
    print(html)

with open('raise_for_status.html', 'w') as html_file:
   html_file.write(html)

# #writing...
# print("writing...")
# file = open('raise_for_status.html', 'wb')     # file.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
# file.write(html.encode('utf-8'))      # 파일에 문자열 저장
# file.close()                     # 파일 객체 닫기


# #reading...
# print("reading...")
# file = open('raise_for_status.html', 'rb')    # file.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
# s = file.read()                  # 파일에서 문자열 읽기
# print(s)                         # Hello, world!
# file.close()                     # 파일 객체 닫기
