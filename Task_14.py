from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

login = driver.find_element(By.NAME, 'username')
login.send_keys('admin')
password = driver.find_element(By.NAME, 'password')
password.send_keys('admin')
inter_button = driver.find_element(By.NAME, 'login')
inter_button.click()
add_country = driver.find_element(By.CSS_SELECTOR, 'a.button').click()


tbody = driver.find_element(By.XPATH, '//*[@id="content"]/form/table[1]/tbody')
links = tbody.find_elements(By.CSS_SELECTOR, 'a')


for x in links:
    try:
        x.get_property('href')
        x.click()
        time.sleep(1)
        switch = driver.window_handles
        driver.switch_to.window(switch[-1])
        driver.close()
        driver.switch_to.window(switch[0])
    except Exception:
        a_link = driver.find_element(By.XPATH, '//*[@id="address-format-hint"]')
        a_link.click()
        switch = driver.switch_to.alert
        switch.accept()




