import time
from webdriver.webdriver import WebDriver


def before_feature(context, feature):
    print("CALLED-HOOK: before_feature: %s" % feature.name)
    context.browser = WebDriver().get()


def after_feature(context, feature):
    print("CALLED-HOOK: after_feature: %s" % feature.name)

    context.browser.quit()
    context.browser = None


def after_step(context, step):
    print("CALLED-HOOK: after_scenario: %s" % step.name)

    time.sleep(5)
