from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.implicitly_wait(3)
wait = WebDriverWait(driver, 3)

driver.get('http://localhost/litecart/en/')

check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
while int(check_count) < 3:
    driver.find_element(By.CSS_SELECTOR, '#box-most-popular > div > ul > li:nth-child(1) > a.link').click()
    driver.find_element(By.CSS_SELECTOR, 'button[name=add_cart_product]').click()
    try:
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[class=content][style]')))
    except Exception:
        Select(driver.find_element(By.CSS_SELECTOR, 'select[name="options[Size]"]')).select_by_value('Small')
        driver.find_element(By.CSS_SELECTOR, 'button[name=add_cart_product]').click()
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name=add_cart_product][style=""')))
    finally:
        driver.back()
        check_count = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text



check_count_ofter_delete = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text
while int(check_count_ofter_delete) != 0:
    driver.find_element(By.CSS_SELECTOR, '#cart a.link').click()
    driver.find_element(By.CSS_SELECTOR, 'button[name=remove_cart_item]').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div [id=checkout-cart-wrapper][style="opacity: 1;"]')))
    driver.back()
    check_count_ofter_delete = driver.find_element(By.CSS_SELECTOR, '#cart > a.content > span.quantity').text








