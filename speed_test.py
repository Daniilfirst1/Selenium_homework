from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.implicitly_wait(5)


driver.get('https://jobb.blocket.se/')
madal = driver.find_element(By.ID, 'accept-ufti')
madal.click()

search = driver.find_element(By.ID, 'whatinput')
search.send_keys('qa engineer')
search_button = driver.find_element(By.ID, 'search-button')
search_button.click()

time.sleep(5)









