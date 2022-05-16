from features.pages.base_page import BasePage
from features.pages.locators import TextBoxLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from features.steps import credentials
from selenium.webdriver.common.action_chains import ActionChains


class TextBoxPage(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.full_name = TextBoxLocators.full_name_css
        self.email = TextBoxLocators.email_css
        self.current_address = TextBoxLocators.current_address_css
        self.permanent_address = TextBoxLocators.permanent_address_css
        self.submit_btn = TextBoxLocators.submit_css
        self.current_name = TextBoxLocators.current_name
        self.current_email = TextBoxLocators.current_email
        self.current_current_address = TextBoxLocators.current_current_address
        self.current_permanent_address = TextBoxLocators.current_permanent_address

    def input_full_name(self, full_name_value):
        self.input_values(self.full_name, full_name_value)

    def input_email(self, email):
        self.input_values(self.email, email)

    def input_current_address(self, current_address):
        self.input_values(self.current_address, current_address)

    def input_permanent_address(self, permanent_address):
        self.input_values(self.permanent_address, permanent_address)

    def click_on_submit_btn(self):
        self.click_on_element(self.submit_btn)

    def return_current_name(self):
        return self.return_text_from_element(self.current_name)

    def return_current_email(self):
        return self.return_text_from_element(self.current_email)

    def return_current_current_address(self):
        return self.return_text_from_element(self.current_permanent_address)

    def return_current_permanent_address(self):
        return self.return_text_from_element(self.current_permanent_address)

    def check_if_name_is_shown(self):
        return self.check_if_element_exists(self.current_name)

    def check_if_email_is_shown(self):
        return self.check_if_element_exists(self.current_email)