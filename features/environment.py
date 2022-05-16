from selenium import webdriver
from features import configuration
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import allure

link = configuration.link
browser = configuration.browser


def before_scenario(context, scenario):
    if browser == 'Chrome':
        context.selenium_driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'Firefox':
        context.selenium_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == 'Edge':
        context.selenium_driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    context.link = link
    context.selenium_driver.maximize_window()


def after_scenario(context, scenario):
#     if scenario.status == 'failed':
#         allure.attach(context.selenium_driver.get_screenshot_as_png(), f"{scenario.name} - FAILED",
#                       allure.attachment_type.PNG)
    context.selenium_driver.quit()
