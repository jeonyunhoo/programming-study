from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81")

pruduct_element = driver.find_elements(By.CLASS_NAME, 'goods_title')
for i in pruduct_element:
    print(i.text)

time.sleep(5)