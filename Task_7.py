from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/en/')

stikers_in_mos_popular = driver.find_elements(By.CSS_SELECTOR, 'li.product.column.shadow.hover-light')
for x in stikers_in_mos_popular:
    assert len(x.find_elements(By.CSS_SELECTOR, 'div.sticker')) == 1


