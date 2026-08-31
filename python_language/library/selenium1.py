from selenium import  webdriver
import time

#크롬브라우저 실행
driver = webdriver.Chrome()
# 주소 접속
driver.get("https://www.naver.com")
# 5초동안 대기
time.sleep(5)
