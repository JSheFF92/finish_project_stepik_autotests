import time

import pytest

from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]


# @pytest.mark.parametrize('link',
#             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                   marks=pytest.mark.xfail),
#                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.parametrize('product_link',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, product_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{product_link}"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_add_basket()
    page.solve_quiz_and_get_code()
    page_basket = ProductPage(browser, browser.current_url)
    page_basket.should_be_basket_url()
    page.name_book()
    page.price_book()
