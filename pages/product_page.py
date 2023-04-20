from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_add_basket(self):
        basket_link = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        basket_link.click()

    def should_be_basket_url(self):
        assert self.browser.current_url

    def name_true_add_book(self):
        book_name_page1 = self.browser.find_element(By.CSS_SELECTOR, 'h1')
        name1 = book_name_page1.text
        book_name_page2 = self.browser.find_element(By.CSS_SELECTOR, '#messages div.alert-success strong')
        name2 = book_name_page2.text
        assert name1 == name2, 'Наименования добавленной книги и книги в корзине разные'

    def price_true_add_book(self):
        price_book_page1 = self.browser.find_element(By.CSS_SELECTOR, 'p.price_color')
        price1 = price_book_page1.text
        price_book_page2 = self.browser.find_element(By.CSS_SELECTOR, 'div.alert-info p strong')
        price2 = price_book_page2.text
        assert price1 == price2, 'Цены добавленной книги и книги в корзине разные'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
            "Success message is presented should be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE_PRICE), \
            "Success message is presented, but should not be"