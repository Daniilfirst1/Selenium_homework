from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')

login = driver.find_element(By.NAME, 'username')
login.send_keys('admin')

password = driver.find_element(By.NAME, 'password')
password.send_keys('admin')

inter_button = driver.find_element(By.NAME, 'login')
inter_button.click()

add_country = driver.find_element(By.CSS_SELECTOR, 'a.button').click()
time.sleep(1)

tbody = driver.find_element(By.XPATH, '//*[@id="content"]/form/table[1]/tbody')

links = tbody.find_elements(By.CSS_SELECTOR, 'a')


for x in links:
    if x.get_property('href') == 
    # x.click()
    time.sleep(1)



# a_link = driver.find_element(By.XPATH, '//*[@id="address-format-hint"]')
# a_link.click()
# time.sleep(2)
# switch = driver.switch_to.alert
# switch.accept()



time.sleep(3)


# i = 2
# while i<len(links)+2:
#     all_outside_links = driver.find_element(By.XPATH, f'//*[@id="content"]/form/table[1]/tbody/tr[{i}]/td/a')
#     if all_outside_links.get_property('href') != None:
#         all_outside_links.click()
#     i+=1