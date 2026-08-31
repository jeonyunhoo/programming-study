from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://comic.naver.com/webtoon?tab=mon")

time.sleep(2)

titles = driver.find_elements(
    By.XPATH, '//span[contains(@class, "ContentTitle__title")]//span[@class="text"]'
)

for i in titles:
    print(i.text)

time.sleep(3)

for i in titles:
    print(i.text)
print(len(titles))

time.sleep(5)