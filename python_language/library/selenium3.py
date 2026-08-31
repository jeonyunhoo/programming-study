from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# driver.get("https://www.naver.com")

# s_element = driver.find_element(By.XPATH, '//*[@id="query"]')

# s_element.send_keys("뉴스")
# s_element.send_keys(Keys.ENTER)

driver.get("https://www.youtube.com/")

s_element = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/div/div/form/input')

s_element.send_keys("뉴스")

btn = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/div/button')
btn.click()

time.sleep(10)