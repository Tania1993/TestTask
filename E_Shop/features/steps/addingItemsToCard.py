import time
from behave import given, when, then

from E_Shop.pages.mainPage import MainPage


@given(u'guest user opens the e-shop with {url}')
def step_impl(context, url):
    context.browser.get(url)


@when(u'user selects a category')
def step_impl(context):
    for row in context.table:
        category = MainPage().select_category(context.browser, row['category'])
        category.click()


@then(u'sorts results by price in desc order')
def step_impl(context):
    price_btn = MainPage().price_sorting(context.browser)
    price_btn.click()

    context.browser.set_page_load_timeout(time_to_wait=5)

    desc_order = MainPage().change_order(context.browser)
    desc_order.click()


@then(u'user adds <count> most expensive items to the card')
def step_impl(context):
    for row in context.table:
        for i in range(int(row['count'])):
            MainPage().add_item(context.browser, i)
            context.browser.back()
            time.sleep(3)