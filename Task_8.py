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

#Part A
rows = driver.find_elements(By.CSS_SELECTOR, 'tr.row td:nth-child(5)')


list_countries = []

def get_textcontent_from_rows(list_countries):
    for x in rows:
        list_countries.append(x.get_property('textContent'))
    assert list_countries == sorted(list_countries)

all_list = get_textcontent_from_rows(list_countries=list_countries)

#Part B

zones = driver.find_elements(By.CSS_SELECTOR, 'tr.row')

list_geozones = []

i = 1
while i<len(zones)+1:
    a = driver.find_element(By.CSS_SELECTOR, f'tr:nth-child({i})')
    d = a.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(6)')
    if int(d.text) >0:
        b = a.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(5)')
        c = b.find_element(By.CSS_SELECTOR, 'a')
        c.click()
        time.sleep(2)
        list_geozones_names = driver.find_elements(By.CSS_SELECTOR, '#table-zones > tbody td:nth-child(3)')
        h = 2
        while h<len(list_geozones_names)-1:
            q = driver.find_element(By.CSS_SELECTOR, f'#table-zones > tbody > tr:nth-child({h}) > td:nth-child(3)')
            list_geozones.append(q.get_property('textContent'))
            h+=1
        assert list_geozones == sorted(list_geozones)
        print(list_geozones)
        list_geozones.clear()
        driver.back()
    i+=1
