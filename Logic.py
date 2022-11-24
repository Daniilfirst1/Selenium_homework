from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
import allure
from allure_commons.types import AttachmentType

driver = webdriver.Chrome()
base_url = 'https://cezarkazan.ru'

class BaseElements:
    
    def __init__(self,driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def go_to_site(self, url=''):
        return self.driver.get(self.base_url + '/' + url)

    def find_element_by_name(self, name):
        return self.driver.find_element(By.NAME, name)

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_element_by_tag_name(self, tag):
        return self.driver.find_element(By.TAG_NAME, tag)


base = BaseElements(driver, base_url)



