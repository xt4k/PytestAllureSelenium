import allure

from pages.models.home_page import HomePage
from tests.base_test_class import BaseTestClass

expected_product_name = "Blackberry"
initial_url = "https://rahulshettyacademy.com/angularpractice/shop"


@allure.epic("Web_Graphic_User_Interface")
@allure.parent_suite("General UI Functionality")
@allure.suite("User_Interface")
@allure.sub_suite("Shop page availability")
@allure.feature("Happy paths validation")
@allure.story("Check home page to shop page navigation")
@allure.label("owner_name", "Yuriy L.")
@allure.label("owner_email", "yuriy.l@e.mail")
@allure.tag("Functional", "Base Test")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("General Functionality test")
@allure.testcase("TMS_LINK-123456")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("JIRA_LINK-123")
@allure.description("This test is navigates from home to shop page and then check goods has correct names")
@allure.description_html("<h1><b>This test is navigates from home to shop page and then check goods has correct names")
class TestOne(BaseTestClass):

    def test_e2e_select(self, test_logger):
        self.logger = test_logger
        self.log_info("run")

        home_page = HomePage(self.driver, self.logger)
        home_page.open_page(initial_url)

        shop_page = home_page.shop_button()
        shop_page.shot_attach("e2e_select_attach1")

        shop_item_list = shop_page.get_items()
        shop_page.shot_attach("e2e_select_attach2")
        self.log_info(f"shop_item_list:`{shop_item_list}`.")

        for element in shop_item_list:
            actual_element_text = shop_page.get_item_name(element)
            image_url = shop_page.get_image_path(element)
            self.log_info(f"element text:`{actual_element_text}`, image_url:`{image_url}`.")

            if actual_element_text == expected_product_name:
                self.log_info(f"actual text:`{actual_element_text}`, expected name:`{expected_product_name}`.")
                assert expected_product_name.lower() in image_url.lower(), f"not found {expected_product_name.lower()} in {image_url.lower()} "

        shop_page.shot_attach("e2e_select_attach3")
        self.log_info("end")
