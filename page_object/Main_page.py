from Base_page import BasePage
from selenium.webdriver.common.by import By

class MainPageLocators:
    LOCATOR_CLICK_PRODUCT = (By.CSS_SELECTOR, '#box-most-popular > div > ul > li:nth-child(1) > a.link')
    LOCATOR_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#cart a.link')
    LOCATOR_CHECK_COUNT = (By.CSS_SELECTOR, '#cart > a.content > span.quantity')
    

class SearchHelper(BasePage):

    def add_product_on_main_page(self):
        search_field = self.find_element(MainPageLocators.LOCATOR_CLICK_PRODUCT)
        search_field.click()
        return search_field

    def click_on_the_checkout_button(self):
        return self.find_element(MainPageLocators.LOCATOR_CHECKOUT_BUTTON).click()

    def check_count_product(self):
        return self.find_element(MainPageLocators.LOCATOR_CHECK_COUNT).text