from selenium import webdriver

path = "C:/programs/webdriver/chromedriver.exe"
driver = webdriver.Chrome(path)

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome('chromedriver', chrome_options=options)

driver.get('http://naver.com')
driver.implicitly_wait(3)
driver.get_screenshot_as_file('naver_main.png')
driver.quit()
