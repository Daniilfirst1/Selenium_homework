from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/en/')

check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
while int(check_count) < 3:
    driver.find_element(By.CSS_SELECTOR, '#box-most-popular > div > ul > li:nth-child(1) > a.link').click()
    driver.find_element(By.CSS_SELECTOR, 'button[name=add_cart_product]').click()
    check_count_wait = WebDriverWait(driver, timeout = 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[class=quantity]"))).text
    print(check_count)
    print(check_count_wait)
    driver.back()
    check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text



check_count_ofter_delete = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
while int(check_count_ofter_delete) != 0:
    driver.find_element(By.CSS_SELECTOR, '#cart a.link').click()
    driver.find_element(By.CSS_SELECTOR, 'button[name=remove_cart_item]').click()
    driver.back()
    check_count_ofter_delete = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text








