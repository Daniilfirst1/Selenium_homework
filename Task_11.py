from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import random
import string
import time

driver = webdriver.Chrome()
driver.implicitly_wait(2)

s = string.ascii_lowercase+string.digits
login_generator = 'ivan'+''.join(random.sample(s,5))
password_generator = ''.join(random.sample(s,15))

my_password = password_generator
my_login = login_generator

driver.get('http://localhost/litecart/en/create_account')


firstname = driver.find_element(By.CSS_SELECTOR, 'input[name=firstname]')
firstname.send_keys('Ivan')

lastname = driver.find_element(By.CSS_SELECTOR, 'input[name=lastname]')
lastname.send_keys('Ivanov')

adress1 = driver.find_element(By.CSS_SELECTOR, 'input[name=address1]')
adress1.send_keys('World')

postcode = driver.find_element(By.CSS_SELECTOR, 'input[name=postcode]')
postcode.send_keys('19019')

city = driver.find_element(By.CSS_SELECTOR, 'input[name=city]')
city.send_keys('NewYork')

list_country = driver.find_element(By.XPATH, '//*[@id="create-account"]/div/form/table/tbody/tr[5]/td[1]/span[2]/span[1]/span/span[2]')
list_country.click()
select_country_2 = driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input')
select_country_2.send_keys('united states', Keys.ENTER)
time.sleep(1)




email_customer = driver.find_element(By.CSS_SELECTOR, 'input[name=email]')
email_customer.send_keys(f'{my_login}@gmail.com')

phone_customer = driver.find_element(By.CSS_SELECTOR, 'input[name=phone]')
phone_customer.send_keys('888888888')

password_customer = driver.find_element(By.CSS_SELECTOR, 'input[name=password]')
password_customer.send_keys(my_password)


confirmed_password_customer = driver.find_element(By.CSS_SELECTOR, 'input[name=confirmed_password]')
confirmed_password_customer.send_keys(my_password)

create_account = driver.find_element(By.CSS_SELECTOR, 'tbody button')
create_account.click()



logout = driver.find_element(By.XPATH, '//*[@id="box-account"]/div/ul/li[4]')
logout_link = logout.find_element(By.TAG_NAME, 'a')
logout_link.click()
time.sleep(1)

input_login = driver.find_element(By.CSS_SELECTOR, 'input[type=text]')
input_login.send_keys(f'{my_login}@gmail.com')

input_password = driver.find_element(By.CSS_SELECTOR, 'input[type=password]')
input_password.send_keys(my_password)


login_inter = driver.find_element(By.XPATH, '//*[@id="box-account-login"]/div/form/table/tbody/tr[4]/td/span/button[1]')
login_inter.click()
time.sleep(1)
logout = driver.find_element(By.XPATH, '//*[@id="box-account"]/div/ul/li[4]')
logout_link = logout.find_element(By.TAG_NAME, 'a')
logout_link.click()
