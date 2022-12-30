from Base_page import BasePage
from selenium.webdriver.common.by import By

class ChectoutPageLocators:
    LOCATOR_REMOVE_PRODUCT = (By.CSS_SELECTOR, 'button[name=remove_cart_item]')
    LOCATOR_WAIT_REMOVE_BUTTON = (By.CLASS_NAME, 'div [id=checkout-cart-wrapper][style="opacity: 1;"]')
    LOCATOR_CHECK_COUNT_AFTER_DELETE = (By.CSS_SELECTOR, '#cart > a.content > span.quantity')
    

class Actions_chekout(BasePage):

    def delete_product_in_checkout(self):
        search_field = self.find_element(ChectoutPageLocators.LOCATOR_REMOVE_PRODUCT)
        search_field.click()
        return search_field

    def wait_element(self):
        return self.find_element(ChectoutPageLocators.LOCATOR_WAIT_REMOVE_BUTTON)

    def check_count_after_delete(self):
        return self.find_element(ChectoutPageLocators.LOCATOR_CHECK_COUNT_AFTER_DELETE).text

    def go_to_back(self):
        return self.go_back()