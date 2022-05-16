from selenium.webdriver.common.by import By


class TextBoxLocators:
    full_name_css = (By.CSS_SELECTOR, '#userName')
    email_css = (By.CSS_SELECTOR, '#userEmail')
    current_address_css = (By.CSS_SELECTOR, '#currentAddress')
    permanent_address_css = (By.CSS_SELECTOR, '#permanentAddress')
    submit_css = (By.CSS_SELECTOR, '.btn.btn-primary')
    current_name = (By.CSS_SELECTOR, '#name')
    current_email = (By.CSS_SELECTOR, '#email')
    current_current_address = (By.CSS_SELECTOR, '#output duv p:nth-child(3)')
    current_permanent_address = (By.CSS_SELECTOR, '#permanentAddress')


