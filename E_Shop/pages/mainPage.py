from selenium.webdriver.common.by import By

from E_Shop.hooks import hooks


class MainPage:
    def select_category(self, webdriver, category_name):
        category = hooks.get_element(webdriver, By.XPATH, f"*//a[contains(text(), '{category_name}')]")[0]
        return category

    def price_sorting(self, webdriver):
        price_btn = hooks.get_element(webdriver, By.XPATH, "*//label[@for='input-sort-1']")[0]
        return price_btn

    def change_order(self, webdriver):
        desc_order_btn = hooks.get_element(webdriver, By.XPATH, "*//li[@class='catalog-sort-list__item direction default']")[0]
        return desc_order_btn

    def add_item(self, webdriver, count):
        item = hooks.get_element(webdriver, By.XPATH, "*//div[@class='catalog-products']/ul/li")[count]
        item.click()
        buy_btn = hooks.get_element(webdriver, By.XPATH, "*//div[@class='product-item__buy']/div[@class='product-item__button']")[0]
        buy_btn.click()
        continue_buying = hooks.get_element(webdriver, By.XPATH, "*//div[@class='link']")[0]
        continue_buying.click()