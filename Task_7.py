from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/en/')

most_popular = driver.find_element(By.ID, 'box-most-popular')
stikers_in_mos_popular = most_popular.find_elements(By.CSS_SELECTOR, 'div li:nth-child(2)')
for x in stikers_in_mos_popular:
    assert len(x.find_elements(By.CSS_SELECTOR, 'div.sticker')) == 1

box_compaings = driver.find_element(By.ID, 'box-campaigns')
stikers_in_box_compaings= most_popular.find_elements(By.CSS_SELECTOR, 'div li')
for x in stikers_in_box_compaings:
    assert len(x.find_elements(By.CSS_SELECTOR, 'div.sticker')) == 1

box_latest_products = driver.find_element(By.ID, 'box-latest-products')
stikers_in_box_latest_products= most_popular.find_elements(By.CSS_SELECTOR, 'div > ul > li:nth-child(1)')
for x in stikers_in_box_latest_products:
    assert len(x.find_elements(By.CSS_SELECTOR, 'div.sticker')) == 1

