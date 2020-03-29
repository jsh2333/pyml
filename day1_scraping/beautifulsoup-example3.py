#------------------------------------------------
# BeautifulSoup example 3
#------------------------------------------------
# 네이버 영화 사이트의 영화 제목을 크롤링
# https://movie.naver.com/movie/sdb/rank/rmovie.nhn

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('http://movie.naver.com/movie/sdb/rank/rmovie.nhn')
res = urlopen(req)
# html = res.read().decode('cp949')
html = res.read().decode('utf-8')

# 영화 제목에는 <div class="tit3"> 태그
bs = BeautifulSoup(html, 'html.parser')
tags = bs.findAll('div', attrs={'class': 'tit3'})

for tag in tags :
    # 검색된 태그에서 a 태그에서 텍스트를 가져옴
    print(tag.a.text)

# 인덱스를 주고 싶다면 enumerate를 사용한다.
for index, tag in enumerate(tags):
   print(str(index) + " : " + tag.a.text)


   