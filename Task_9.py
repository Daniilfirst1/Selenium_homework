from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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


list_geozones = []
x = [2, 3]

for i in x:
    countries = driver.find_element(By.XPATH, f'//*[@id="content"]/form/table/tbody/tr[{i}]/td[3]')
    link = countries.find_element(By.CSS_SELECTOR, 'a').click()
    time.sleep(1)
    count_zones = driver.find_elements(By.CSS_SELECTOR, 'select.select2-hidden-accessible')
    len_zones = len(count_zones)+2
    for x in range(len_zones)[2:]:
        zones = Select(driver.find_element(By.XPATH, f'//*[@id="table-zones"]/tbody/tr[{x}]/td[3]/select'))
        z = zones.first_selected_option
        list_geozones.append(zones.first_selected_option.text)
    assert list_geozones == sorted(list_geozones)
    list_geozones.clear()
    driver.back()
    


    
    






    
    


