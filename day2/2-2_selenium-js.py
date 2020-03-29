
import time
from selenium import webdriver

path = "C:/programs/webdriver/chromedriver.exe"
driver = webdriver.Chrome(path)

# 적당한 웹 페이지 열기
driver.get("https://google.com")

# 자바스크립트 실행하기
r = driver.execute_script("return 100 + 50")
print(r)
