from Base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPageLocators:
    LOCATOR_ADD_PRODUCT = (By.CSS_SELECTOR, 'button[name=add_cart_product]')
    LOCATOR_WAIT_ADD_BUTTON = (By.CLASS_NAME, 'button[name=add_cart_product]')
    LOCATOR_CLICK_SIZE = (By.CSS_SELECTOR, 'select[name="options[Size]"]')
    

class Actions(BasePage):

    def add_product_in_product(self):
        search_field = self.find_element(ProductPageLocators.LOCATOR_ADD_PRODUCT)
        search_field.click()
        return search_field

    def add_smal_size(self, size):
        size_product = self.find_element(ProductPageLocators.LOCATOR_CLICK_SIZE)
        size.select_by_value(size)
        return size_product

    def wait_element(self):
        return self.find_element(ProductPageLocators.LOCATOR_WAIT_ADD_BUTTON)

    def go_to_back(self):
        return self.go_back()