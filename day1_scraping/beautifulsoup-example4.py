#------------------------------------------------
# BeautifulSoup example 4
#------------------------------------------------
# 굽네치킨 매장 정보
# http://www.goobne.co.kr/store/search_store.jsp

import os
import time
from selenium import webdriver
from itertools import count
from bs4 import BeautifulSoup
import pandas as pd             # pandas 라이브러리

def crawling_goobne():
    url = 'http://www.goobne.co.kr/store/search_store.jsp'

    # \U는 유니코드로 인식되기 때문에 \\U와 같이 escape 처리했다.
    path = "C:/programs/chromedriver/chromedriver.exe"
    wd = webdriver.Chrome(path)
    wd.get(url)

    
    RESULT_DIRECTORY = 'c:/crawling'
    results = []
    for page in count(1):
        script = 'store.getList(%d)' % page  # 굽네치킨에서 사용하는 페이지를 이동시키는 js 코드
        wd.execute_script(script)  # js 실행
        time.sleep(5)              # 크롤링 로직을 수행하기 위해 5초정도 쉬어준다.

        html = wd.page_source
        bs = BeautifulSoup(html, 'html.parser')
        tag_body = bs.find('tbody', attrs={'id': 'store_list'})
        tags_tr = tag_body.findAll('tr')
        print(tags_tr)

        if tags_tr[0].get('class') is None:  # 맨 마지막 페이지인 102에서는 class='on lows'가 없다. => 종료 조건
            print(tags_tr[0])
            print("= class none = ")
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[6]
            results.append((name, address))

    table = pd.DataFrame(results, columns=['name', 'address'])
    table.to_csv('{0}/table_goobne.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w')
    #table.to_csv('./ch01/table_goobne.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w')
    wd.close()

crawling_goobne()    
cwd = os.getcwd()