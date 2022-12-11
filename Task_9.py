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


x = [2, 3]

for i in x:
    countries = driver.find_element(By.XPATH, f'/html/body/div/div/div/table/tbody/tr/td[3]/form/table/tbody/tr{i}]/td[3]')
    link = countries.find_element(By.CSS_SELECTOR, 'a').click()
    time.sleep(2)
    count_zones = driver.find_elements(By.CSS_SELECTOR, 'select.select2-hidden-accessible')
    len_zones = len(count_zones)
    for x in range(len_zones)[2:]:
        zones = driver.find_element(By.XPATH, f'//*[@id="table-zones"]/tbody/tr[{x}]/td[3]/select').text




        




# countries = driver.find_element(By.CSS_SELECTOR, 'form')

# link = countries.find_elements(By.CSS_SELECTOR, 'a')

# for x in link:
#     x.click()
#     zones = driver.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(3)')
#     for x in zones:
#         print(x.get_attribute('value'))

    
    






    
    


