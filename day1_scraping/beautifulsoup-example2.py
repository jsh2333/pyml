#------------------------------------------------
# BeautifulSoup example 2
#------------------------------------------------
 
 # package import
from bs4 import BeautifulSoup

html = '<td id="td1" class="title">' \
       '  <div class="tit3">' \
       '    <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>' \
       '  </div>' \
       '</td>'
  

# 1. 조회
def ex1():
    # BeautifulSoup객체생성 ( html문자열, 파싱방법을 지정 )
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs))
    # <td id="td1" class="title"><div class="tit3"><a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a></div></td> <class 'bs4.BeautifulSoup'>

    # a 태그 출력
    tag = bs.a
    print(tag, type(tag))
    # <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a> <class 'bs4.element.Tag'>

ex1()

# 2. Attribute 값 받아오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])     # ['title']     => 리스트
    print(tag['id'])        # td1
    print(tag.attrs)        # {'id': 'td1', 'class': ['title']}   => 딕셔너리

    tag = bs.div
    print(tag['id'])        # id가 없으므로 error

ex2()

# 3. Attribute 검색
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    # div 태그 중, class가 tit3인 태그를 찾는다.
    tag = bs.find('div', attrs={'class': 'tit3'})
    print(tag)      # <div class="tit3"> <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a> </div>

    tag = bs.find('div')
    print(tag)      # <div class="tit3"> <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a> </div>

    # 없는 태그를 조회할 경우
    tag = bs.find('td', attrs={'class': 'not_exist'})
    print(tag)      # None

    # 전체 태그에 대해 title이 범죄도시인 태그를 찾는다.
    tag = bs.find(attrs={'title': '범죄도시'})
    print(tag)      # <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>

ex3()
# 4. select(), content() 메서드
def ex4():
    bs = BeautifulSoup(html, 'html.parser')

    # CSS 처럼 셀렉터를 지정할 수 있다.
    tag = bs.select("td div a")[0]
    print(tag)        # <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>

    text = tag.contents[0]
    print(text)     # 범죄도시


# 5. extract() 메서드
def ex5():
    bs = BeautifulSoup(html, 'html.parser')
    tag = bs.select("td")[0]
    print(tag)      # <td class="title" id="td1"> <div class="tit3"> <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a> </div></td>

    # div요소를 제거
    div_elements = tag.find_all("div")
    for div in div_elements:
        div.extract()
        
    print(tag)      # <td class="title" id="td1"> </td>