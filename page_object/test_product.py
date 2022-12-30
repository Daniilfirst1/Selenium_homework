from Product_page import Actions
from Checkout_page import Actions_chekout
from Main_page import SearchHelper
from selenium.webdriver.support.ui import Select
import time


def test(browser):
    main_page = SearchHelper(browser)
    product_page = Actions(browser)
    chectout_page = Actions_chekout(browser)
    main_page.go_to_site()
    check_count = main_page.check_count_product()
    while int(check_count)<3:
        main_page.add_product_on_main_page()
        product_page.add_product_in_product()
        try:
            product_page.wait_element()
        except Exception:
            time.sleep(1)
        finally:
            product_page.go_back()
            check_count = main_page.check_count_product()

    chect_count_after = chectout_page.check_count_after_delete()
    while int(chect_count_after) != 0:
        main_page.click_on_the_checkout_button()
        chectout_page.delete_product_in_checkout()
        time.sleep(1)
        chectout_page.go_back()
        chect_count_after = chectout_page.check_count_after_delete()


