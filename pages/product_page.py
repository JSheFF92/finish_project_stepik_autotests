from selenium.webdriver.common.by import By

from .base_page import BasePage


class ProductPage(BasePage):
    def go_to_add_basket(self):
        basket_link = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        basket_link.click()

    def should_be_basket_url(self):
        assert self.browser.current_url


    def name_book(self):
        book_name1 = self.browser.find_element(By.CSS_SELECTOR, 'h1')
        name1 = book_name1.text
        book_name2 = self.browser.find_element(By.CSS_SELECTOR, '#messages div.alert-success strong')
        name2 = book_name2.text
        assert name1 == name2, 'Наименования добавленной книги и книги в корзине разные'

    def price_book(self):
        price_book1 = self.browser.find_element(By.CSS_SELECTOR, 'p.price_color')
        price1 = price_book1.text
        price_book2 = self.browser.find_element(By.CSS_SELECTOR, 'div.alert-info p strong')
        price2 = price_book2.text
        assert price1 == price2, 'Цены добавленной книги и книги в корзине разные'

