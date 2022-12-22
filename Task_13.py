from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/en/')

check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
while int(check_count) < 3:
    driver.find_element(By.CSS_SELECTOR, '#box-most-popular > div > ul > li:nth-child(1) > a.link').click()
    driver.find_element(By.CSS_SELECTOR, 'button[name=add_cart_product]').click()
    time.sleep(1)
    driver.back()
    check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text



check_count_ofter_delete = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
while int(check_count_ofter_delete) != 0:
    driver.find_element(By.CSS_SELECTOR, '#cart a.link').click()
    driver.find_element(By.CSS_SELECTOR, 'button[name=remove_cart_item]').click()
    time.sleep(1)
    driver.back()
    check_count_ofter_delete = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text








