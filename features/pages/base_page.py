from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(element))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(element)
        )
        self.driver.find_element(*element).click()

    def return_text_from_element(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(element))
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(element))
        return self.driver.find_element(*element).text

    def input_values(self, element, value):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(element)
        )
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)

    def check_if_element_exists(self, elem):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located(elem))
            return len(self.driver.find_elements(*elem)) > 0
        except TimeoutException:
            return False

    def get_text_from_input_field(self, element):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(element)
        )
        return self.driver.find_element(*element).get_attribute('value')


