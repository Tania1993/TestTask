from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_element(webdriver, locator, name):
    return WebDriverWait(webdriver, timeout=5).until(EC.presence_of_all_elements_located((locator, name)))
