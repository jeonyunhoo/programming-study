from selenium import  webdriver
import time
from selenium.webdriver.common.by import By

#크롬브라우저 실행
driver = webdriver.Chrome()
# 주소 접속from selenium import  webdriver
import time
from selenium.webdriver.common.by import By

#크롬브라우저 실행
driver = webdriver.Chrome()
# 주소 접속
driver.get("https://www.example.com")

p = driver.find_element(By.TAG_NAME, 'p')
print("p태그 첫번째 요소 가져옴")
print(p)
print(type(p))
print(p.text)
driver.get("https://www.example.com")

p = driver.find_element(By.TAG_NAME, 'p')
print("p태그 첫번째 요소 가져옴")
print(p)
print(type(p))
print(p.text)