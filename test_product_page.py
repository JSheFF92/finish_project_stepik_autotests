from datetime import time

import faker
import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.parametrize('product_link',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10 + 1)])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, product_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{product_link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.go_to_add_basket()
    page.solve_quiz_and_get_code()
    page_basket = ProductPage(browser, browser.current_url)
    page_basket.should_be_basket_url()
    page.name_true_add_book()
    page.price_true_add_book()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = str(time()) + '123456789'
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.go_to_add_basket()
        page.solve_quiz_and_get_code()
        page_basket = ProductPage(browser, browser.current_url)
        page_basket.should_be_basket_url()
        page.name_true_add_book()
        page.price_true_add_book()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
