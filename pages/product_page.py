from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_add_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_basket_url(self):
        assert self.browser.current_url

    def name_true_add_book(self):
        book_name_page1 = self.browser.find_element(*ProductPageLocators.BOOK_PAGE_NAME1)
        name1 = book_name_page1.text
        book_name_page2 = self.browser.find_element(*ProductPageLocators.BOOK_PAGE_NAME2)
        name2 = book_name_page2.text
        assert name1 == name2, 'Наименования добавленной книги и книги в корзине разные'

    def price_true_add_book(self):
        price_book_page1 = self.browser.find_element(*ProductPageLocators.SUCCES_MESSAGE_PRICE)
        price1 = price_book_page1.text
        price_book_page2 = self.browser.find_element(*ProductPageLocators.SUCCES_MESSAGE)
        price2 = price_book_page2.text
        assert price1 == price2, 'Цены добавленной книги и книги в корзине разные'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
            "Success message is presented should be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE_PRICE), \
            "Success message is presented, but should not be"