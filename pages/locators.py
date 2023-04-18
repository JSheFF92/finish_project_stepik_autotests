from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    SUCCES_MESSAGE = (By.CSS_SELECTOR, 'div.alert-info p strong')
    SUCCES_MESSAGE_PRICE = (By.CSS_SELECTOR, 'p.price_color')