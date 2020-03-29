import time
from selenium import webdriver

path = "C:/programs/webdriver/chromedriver.exe"
driver = webdriver.Chrome(path)

# chrome 실행하기 --- (※1)
options = webdriver.ChromeOptions()
# options.add_argument("headless")
# browser = webdriver.Chrome('chromedriver', chrome_options=options)

print("webdriver")
print(browser)

exit()
#-----------------------------------------

USER = "<아이디>"
PASS = "<비밀번호>"


# 로그인 페이지에 접근하기 --- (※2)
url_login = "https://www.aladin.co.kr/login/wlogin_popup.aspx?SecureOpener=1"
browser.get(url_login)
print("로그인 페이지에 접근합니다.")


U

# 텍스트 박스에 아이디와 비밀번호 입력하기 --- (※3)
e = browser.find_element_by_id("Email")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("Password")
e.clear()
e.send_keys(PASS)

time.sleep(3)

# 입력 양식 전송해서 로그인하기 --- (※4)
form = browser.find_element_by_css_selector("div.left1_right > a")
form.submit()

# a link의 url 주소가 없는 경우 클릭실행이 되지 않는 경우가 있다
# browser = webdriver.Chrome()
# form.click()

# 첫번째 방법
# form.send_keys('\n')    # 해당 링크/명령어 에  엔터를 실행하도록

# # 두 번째 방법
# driver.execute_script("arguments[0].click();", form)  #자바스크립트 실행


print("로그인 버튼을 클릭합니다.")
time.sleep(3)
# 쇼핑 페이지의 데이터 가져오기 --- (※5)
print("naver shopping url 접속")
browser.get("https://www.aladin.co.kr/account/wmaininfo.aspx?pType=OrdersHistoryList&start=we")
print("naver shopping url 데이터 가져오기")
time.sleep(3)

file = open('aladin_shopping_list.txt', 'w')     # file.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
print("writing - aladin-shopping-list.txt...")
# 쇼핑 목록 출력하기 --- (※6)
products = browser.find_elements_by_css_selector(".td_left_item")
print(products)
for product in products:
  print("-", product.text)
  #writing...
  file.write('{0}\n'.format(product.text))      # 파일에 문자열 저장
file.close()                     # 파일 객체 닫기

# reading...
print("reading...")
with open('aladin_shopping_list.txt', 'r') as file:    # file.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력