from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    SUCCES_MESSAGE = (By.CSS_SELECTOR, 'div.alert-info p strong')
    SUCCES_MESSAGE_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    BOOK_PAGE_NAME1 = (By.CSS_SELECTOR, 'h1')
    BOOK_PAGE_NAME2 = (By.CSS_SELECTOR, '#messages div.alert-success strong')
    BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")