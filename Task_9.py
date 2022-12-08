from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')

login = driver.find_element(By.NAME, 'username')
login.send_keys('admin')

password = driver.find_element(By.NAME, 'password')
password.send_keys('admin')

inter_button = driver.find_element(By.NAME, 'login')
inter_button.click()


countries = driver.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(5)')

link = countries.find_elements(By.CSS_SELECTOR, 'a')

for x in link:
    x.click()
    zones = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(3)')
    for x in zones:
        print(x.get_attribute('value'))
        


time.sleep(4)

#table-zones > tbody > tr:nth-child(2)
#table-zones > tbody > tr:nth-child(2) > td:nth-child(3) > select

    
    






    
    


