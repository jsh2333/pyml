
#------------------------------------------------
# 네이버금융 환율정보 추출하기
#------------------------------------------------
# 다양한 금융 정보가 공개되어 있는 “네이버 금융“ 에서 원/달러 환율 정보를 추출합니다.
# http://info.finance.naver.com/marketindex/

from bs4 import BeautifulSoup
import urllib.request as req
# HTML 가져오기
# url = "http://info.finance.naver.com/marketindex/"
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)
# HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
# 원하는 데이터 추출하기 --- (※1)
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)