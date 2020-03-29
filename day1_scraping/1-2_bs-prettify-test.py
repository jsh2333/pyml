from bs4 import BeautifulSoup 
html = """
<html><body>
  <ul>
    <li>
      <p>
      <a href="http://www.naver.com"> 
        test 
      </a>
      </p></li>
    <li><a href="http://www.daum.net">daum</a></li>
  </ul>
</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
# 분석이 제대로 됐는지 확인 --- (※1)
soup.prettify()
a = soup.p.a
# attrs 속석의 자료형 확인 --- (※2)
type(a.attrs)

#href 속성이 있는지 확인
'href' in a.attrs

# href 속성값 확인
a['href']