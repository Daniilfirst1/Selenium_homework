from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import time


driver = webdriver.Chrome()
driver.implicitly_wait(3)


driver.get('http://localhost/litecart/')

compaings = driver.find_element(By.ID, 'box-campaigns')
product_main_page = compaings.find_element(By.CSS_SELECTOR, 'div li')

name_product_main_page = product_main_page.find_element(By.CSS_SELECTOR, 'div.name')
action_price_product_main_page = product_main_page.find_element(By.CSS_SELECTOR, 'div.price-wrapper > strong')
usually_price_product_main_page = product_main_page.find_element(By.CSS_SELECTOR, 'div.price-wrapper > s')

name_main = name_product_main_page.text
name_action_price_main = action_price_product_main_page.text
name_usually_price_main = usually_price_product_main_page.text

color_name_action_price_main = action_price_product_main_page.value_of_css_property('color')



link_click = product_main_page.find_element(By.CSS_SELECTOR, 'a').click()


name_product_insaide_main = driver.find_element(By.TAG_NAME, 'h1')
action_price_product_inside_page = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper > strong')
usually_price_product_inside_page = driver.find_element(By.CSS_SELECTOR, 'div.price-wrapper > s')

name_inside = name_product_insaide_main.text
name_action_price_inside = action_price_product_inside_page.text
name_usually_price_inside = usually_price_product_inside_page.text

color_name_action_price_inside = action_price_product_inside_page.value_of_css_property('color')


def test_name(name_product_main_page, name_product_insaide_main):
    assert name_product_main_page == name_product_insaide_main

def test_action_price(name_action_price_main, name_action_price_inside):
    assert name_action_price_main == name_action_price_inside

def test_usually_price(name_usually_price_main, name_usually_price_inside):
    assert name_usually_price_main == name_usually_price_inside

def test_action_color(color_name_action_price_inside, color_name_action_price_main):
    color_action_main = Color.from_string(color_name_action_price_main).rgba
    color_action_split = color_action_main.split(', ')
    assert color_action_split[1:3] == ['0', '0']
    color_action_inside = Color.from_string(color_name_action_price_inside).rgba
    color_action_split = color_action_inside.split(', ')
    assert color_action_split[1:3] == ['0', '0']


test_name(name_main, name_inside)
test_action_price(name_action_price_main, name_action_price_inside)
test_usually_price(name_usually_price_main, name_usually_price_inside)
test_action_color(color_name_action_price_main, color_name_action_price_inside)

driver.quit()




