import time

import allure

from pages.base_page import BasePage
from pages.locators.cart_page import CartPageLocators
from pages.models.plants_cart_page import PlantsCartPage
from tests.base_test_class import BaseTestClass

start_page = "https://rahulshettyacademy.com/seleniumPractise/#/"
promo_code_valid = "rahulshettyacademy"
search_pattern = "ber"
expected_list = ["Cucumber", "Raspberry", "Strawberry"]


@allure.epic("Web_Graphic_User_Interface")
@allure.parent_suite("Advanced UI Functionality")
@allure.suite("User_Interface")
@allure.sub_suite("Table search availability")
@allure.feature("Search in table and discount validation")
@allure.story("Check if prodyuct can be found in table")
@allure.label("owner_name", "John Smith")
@allure.label("owner_email", "j.smith.l@e.mail")
@allure.tag("Functional", "Searching Test")
@allure.severity(allure.severity_level.MINOR)
@allure.title("Supplementary Functionality test")
@allure.testcase("TMS_LINK-123327")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("JIRA_LINK-3251")
@allure.description("This test is is searching products in table and then apply discount to them")
@allure.description_html(
    "<h1><b>This test is is searching products in table and then apply discount to them")
class TestThird(BaseTestClass):
    def test_e2e_third(self, test_logger):
        self.logger = test_logger
        self.log_info("run")

        BasePage(self.driver, self.logger).open_page(start_page)

        plants_cart_page = PlantsCartPage(self.driver, self.logger)
        plants_cart_page.shot_to("e2e_po_3_1")

        plants_cart_page.text_search(search_pattern)
        time.sleep(2)
        results = plants_cart_page.get_plants()

        exercise_list = plants_cart_page.get_product_names()
        self.log_info(f"exercise_list size: {len(exercise_list)}")
        for text_element in exercise_list:
           # self.logger(f"here is product name `{text_element.text}`")
            assert search_pattern in text_element.text
            check = any(item in text_element.text for item in expected_list)
            self.log_info(f"Check result: {check}")
            assert check

        for found_item in results:
            self.log_info(f"found element with text:`{found_item.text}`.")
            plants_cart_page.add_to_cart(found_item)

        cart_popup = plants_cart_page.go_cart()
        cart_popup.shot_to("e2e_po_3_4")

        cart_page = cart_popup.proceed_to_checkout()
        time.sleep(2)

        cart_page.shot_to("e2e_po_3_5")
        page_sum = int(cart_page.get_total_amount())
        prices = cart_page.get_prices()
        price_from_cell = 0
        for price in prices:
            price_from_cell = price_from_cell + int(price.text)

        self.log_info(f"From table cell:`{price_from_cell}`")
        self.log_info(f"From Summary cell :`{page_sum}`")

        assert price_from_cell == page_sum

        cart_page.set_promo_code(promo_code_valid)
        cart_page.shot_to("e2e_po_3_7")
        cart_page.apply_promo_code()
        cart_page.shot_to("e2e_po_3_8")
        self.verify_element_presence(CartPageLocators.PROMO_INFO)
        cart_page.shot_to("e2e_po_3_9")

        discount_percent = int(cart_page.get_discount_percent())
        page_sum_discounted = float(cart_page.get_sum_discounted())

        self.log_info(f"float price with/without discount `{page_sum_discounted}`/`{page_sum}`")
        self.log_info(f"Total amount with/without discount:`{page_sum_discounted}`/`{discount_percent}`")

        result_sum = page_sum * (1 - discount_percent / 100)
        self.log_info(f"process summary:`{result_sum}`")

        assert page_sum_discounted < page_sum
        assert page_sum_discounted == page_sum_discounted
        self.log_info("end")
