from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/admin/')

login = driver.find_element(By.NAME, 'username')
login.send_keys('admin')

password = driver.find_element(By.NAME, 'password')
password.send_keys('admin')

inter_button = driver.find_element(By.NAME, 'login')
inter_button.click()

menu_all = driver.find_elements(By.XPATH, '//*[@id="app-"]/a')

i = 1
while i<len(menu_all)+1:
    a = driver.find_element(By.XPATH, f'/html/body/div/div/div/table/tbody/tr/td[1]/div[3]/ul/li[{i}]/a')
    text = a.get_attribute('textContent')
    assert text != None
    a.click()
    x = len(driver.find_elements(By.CSS_SELECTOR, 'li li'))
    if x != 0:
        for m in range(x)[1:]:
            b = driver.find_element(By.XPATH, f'/html/body/div/div/div/table/tbody/tr/td[1]/div[3]/ul/li[{i}]/ul/li[{m}]/a')
            text2 = b.get_attribute('textContent')
            assert text2 != None
            b.click()
    i+=1             
    


    

    

