from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class BasketPage(BasePage):


    def check_product_to_basket(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, 'div.basket-title.hidden-xs')
        except NoSuchElementException:
            return True
        return False

    def assert_check_product_to_basket(self):
        assert self.check_product_to_basket(), "Корзина не пуста"

    def check_text_basket_is_empty(self):
        try:
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='content_inner']/p")))
        except TimeoutException:
            return True
        return False

    def assert_check_text_basket_is_empty(self):
        assert self.check_text_basket_is_empty() == False, "Отсутсвует текст о пустой корзине"