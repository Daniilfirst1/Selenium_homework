from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/en/')


def buy_product(locator1, locator2):
    driver.find_element(By.CSS_SELECTOR, f'{locator1}').click()
    driver.find_element(By.CSS_SELECTOR, f'{locator2}').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
    return check_count


while int(buy_product('#box-most-popular > div > ul > li:nth-child(1) > a.link', 'button[name=add_cart_product]'))<3:
    buy_product('#box-most-popular > div > ul > li:nth-child(1) > a.link', 'button[name=add_cart_product]')
    


def delete_product(locator1):
    driver.find_element(By.CSS_SELECTOR, '#cart a.link').click()
    driver.find_element(By.CSS_SELECTOR, f'{locator1}').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
    return check_count


while int(delete_product('button[name=remove_cart_item]')) != 0:
    delete_product('button[name=remove_cart_item]')





