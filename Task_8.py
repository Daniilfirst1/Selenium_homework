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

zones = driver.find_elements(By.CSS_SELECTOR, 'tr.row td:nth-child(6)')


list_geozones = []

i = 1
while i<len(zones)+1:
    a = driver.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(6)')
    b = x.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(5)')
    c = b.find_element(By.CSS_SELECTOR, 'a')
    c.click()
    x = driver.find_element(By.XPATH, f'//*[@id="table-zones"]/tbody/tr[2]/td[3]')
    list_geozones.append(x.get_property('textContent'))
    print(list_geozones)
    driver.back()
    time.sleep(2)
    i+=1
        



# for x in zones:
#     a = x.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(6)')
#     if int(a.text) > 0:
#         b = x.find_element(By.CSS_SELECTOR, 'tr.row td:nth-child(5)')
#         c = b.find_elements(By.CSS_SELECTOR, 'a')
#         for x in c:
#             x.click()
#             sort_inside_part = driver.find_element(By.CSS_SELECTOR, 'table table#table-zones')
#             sort_inside = sort_inside_part.find_elements(By.CSS_SELECTOR, 'tr td:nth-child(3)')
#             for x in sort_inside:
#                 list_geozones.append(x.get_property('textContent'))
#                 print(list_geozones)
#             driver.back()
#             time.sleep(2)







