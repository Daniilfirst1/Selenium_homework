from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog')

chech_count_before_add = len(driver.find_elements(By.CSS_SELECTOR, 'tr.row'))

login = driver.find_element(By.NAME, 'username')
login.send_keys('admin')
password = driver.find_element(By.NAME, 'password')
password.send_keys('admin')
inter_button = driver.find_element(By.NAME, 'login')
inter_button.click()


add_new_product = driver.find_element(By.CSS_SELECTOR, 'a.button:nth-child(2)')
add_new_product.click()
general_name = driver.find_element(By.CSS_SELECTOR, 'input[name="name[en]"]')
general_name.send_keys('Product#1')
general_code = driver.find_element(By.CSS_SELECTOR, 'input[name=code]')
general_code.send_keys(12012)
general_enable = driver.find_element(By.CSS_SELECTOR, 'label:nth-child(3)').click()
general_product_groups = driver.find_element(By.CSS_SELECTOR, 'input[name="product_groups[]"][value="1-3"')
general_product_groups.click()
general_foto = driver.find_element(By.CSS_SELECTOR, 'input[type=file]')
general_foto.send_keys(os.getcwd()+'/1.png')
general_date_from = driver.find_element(By.CSS_SELECTOR, 'input[name=date_valid_from]')
general_date_from.send_keys('01012022')
general_date_to = driver.find_element(By.CSS_SELECTOR, 'input[name=date_valid_to]')
general_date_to.send_keys('31122022')



information = driver.find_element(By.CSS_SELECTOR, '#content > form > div > ul > li:nth-child(2) > a')
information.click()
information_manifactory = Select(driver.find_element(By.CSS_SELECTOR, 'select[name=manufacturer_id]')).select_by_value('1')
information_keywords = driver.find_element(By.CSS_SELECTOR, 'input[name=keywords]')
information_keywords.send_keys('product, shop')
information_short_description = driver.find_element(By.CSS_SELECTOR, 'input[name="short_description[en]"]')
information_short_description.send_keys('product for everyone')
information_description = driver.find_element(By.CSS_SELECTOR, 'div[class=trumbowyg-editor]')
information_description.send_keys('best product')



prices = driver.find_element(By.CSS_SELECTOR, '#content > form > div > ul > li:nth-child(4) > a')
prices.click()
prices_sum = driver.find_element(By.CSS_SELECTOR, 'input[name=purchase_price]')
prices_sum.clear()
prices_sum.send_keys(100)
prices_currency = Select(driver.find_element(By.CSS_SELECTOR, 'select[name=purchase_price_currency_code]')).select_by_value('USD')
prices_usd = driver.find_element(By.CSS_SELECTOR, 'input[name="prices[USD]"]')
prices_usd.send_keys(100)
prices_euro = driver.find_element(By.CSS_SELECTOR, 'input[name="prices[EUR]"]')
prices_euro.send_keys(80)

save_button = driver.find_element(By.CSS_SELECTOR, 'button[name=save]')
save_button.click()

chech_count_after_add = len(driver.find_elements(By.CSS_SELECTOR, 'tr.row'))
if int(chech_count_before_add) < int(chech_count_after_add):
    pass
else:
    driver.find_element(By.CSS_SELECTOR, 'tr.rowwe')