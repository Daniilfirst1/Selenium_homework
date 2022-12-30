import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


base = DesiredCapabilities.CHROME
base['ms:loggingPrefs'] = { 'browser':'ALL' }


@pytest.fixture
def driver(request):
    drive = webdriver.Chrome()
    request.addfinalizer(drive.quit)
    return drive


def test_logs(driver):
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    username = driver.find_element(By.NAME, "username")
    username.send_keys("admin")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("admin")
    login = driver.find_element(By.NAME, "login")
    login.click()
    m = len(driver.find_elements(By.XPATH, "//td[3]/a[contains(@href, 'edit_product')]"))
    for i in range(4, m+5):
        driver.find_element(By.CSS_SELECTOR, f'#content > form > table > tbody > tr:nth-child({i}) > td:nth-child(3) > a').click()
        for l in driver.get_log("browser"):
            print(l)
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")