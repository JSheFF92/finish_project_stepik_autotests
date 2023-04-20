from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_elementPresent(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_elementPresent(*LoginPageLocators.REGISTRATION_FORM), "Registtration form is not presented"

    def register_new_user(self, email, password):
        newmail = self.browser.find_element(By.CSS_SELECTOR, '[id=id_registration-email]')
        newmail.send_keys(email)
        newpassword1 = self.browser.find_element(By.CSS_SELECTOR, '[id=id_registration-password1]')
        newpassword1.send_keys(password)
        newpassword2 = self.browser.find_element(By.CSS_SELECTOR, '[id=id_registration-password2]')
        newpassword2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()