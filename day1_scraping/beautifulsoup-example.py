#------------------------------------------------
# BeautifulSoup example 
#------------------------------------------------
 
 # package import
from bs4 import BeautifulSoup
import os
os.getcwd()
# 1) html 파일 열기
with open("./ch01/example.html") as fp:
  soup = BeautifulSoup(fp, 'html.parser')
soup
  

# 2) urllib를 통해서 웹에 있는 소스 가져오기
import urllib.request
import urllib.parse

# web_url에 원하는 웹의 URL을 넣어주시면 됩니다.
os.getcwd()
# web_url = "./ch01/example.html"
web_url = "https://news.v.daum.net/v/20200321131028118"
with urllib.request.urlopen(web_url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')    
soup

# 3) requests를 통해서 웹에 있는 소스 가져오기
import requests

# web_url에 원하는 웹의 URL을 넣어주시면 됩니다.
web_url = "https://news.v.daum.net/v/20200321131028118"
r = requests.get(web_url)
r.status_code
r.headers['content-type']
r.encoding
r.text


# 4) find() 및 find_all()함수
# 함수 인자로는 찾고자 하는 태그의 이름, 속성 기타 등등이 들어간다.
# find_all(name, attrs, recursive, string, limit, **kwargs)
# find(name, attrs, recursive, string, **kwargs)

# 4-1) find_all() : 해당 조건에 맞는 모든 태그들을 가져온다.
with open("./ch01/example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    all_divs = soup.find_all("div")
    print(all_divs)


# 4-2) find() : 해당 조건에 맞는 하나의 태그를 가져온다. 
# 중복이면 가장 첫 번째 태그를 가져온다.  
html = "./ch01/example.html"
with open(html) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    first_div = soup.find("div")
    print(first_div)


# 4-3) 태그를 이용해서 가져오기
# 예제 : 모든 <p> 태그들을 가져오기    
html = "./ch01/example.html"
with open(html) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    all_ps = soup.find_all("p")
    print(all_ps)

# 4-4) 예제 : 첫번째 <div>태그를 가져오기
html = "./ch01/example.html"
with open(html) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    first_div = soup.find("div")
    print(first_div)

# 태그와 속성을 이용해서 가져오기

# 태그와 속성을 이용할 때 함수의 인자로 원하는 태그를 첫번째 인자로 
# 그 다음에 속성:값의 형태로 dictionary 형태로 만들어서 넣어주면 된다.

# find_all('태그명', {'속성명' : '값' ...})
# find('태그명', {'속성명' : '값' ...})

# HTML 구조를 이용해 원하는 부분 가져오기
# 예제 4-5) : <div> 태그에서 id속성의 값이 ex_id 인 것을  찾기
html = "./ch01/example.html"
with open(html) as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    ex_id_divs = soup.find('div', {'id' : 'ex_id'})
    print(ex_id_divs)     

# 예제 4-6) : id속성의 값이 ex_id인 <div> 태그에서 <p>태그들만 가져오기
with open("example.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    # id=ex_id인 div 태그를 가져와서
    ex_id_divs = soup.find("div", {"id":"ex_id"})
    # 그 태그들 안에서 p 태그를 가져온다.
    all_ps_in_ex_id_divs = ex_id_divs.find_all("p")
    print(all_ps_in_ex_id_divs)       