import allure
import pytest

from pages.base_page import BasePage
from pages.models.home_page import HomePage
from test_data.home_page_data import HomePageData
from tests.base_test_class import BaseTestClass

home_page_url = "https://rahulshettyacademy.com/angularpractice/"

@allure.epic("Web_Graphic_User_Interface")
@allure.parent_suite("General UI Functionality")
@allure.suite("User_Interface")
@allure.sub_suite("Form submission availability")
@allure.feature("Form submission validation")
@allure.story("Check form submission")
@allure.label("owner_name", "XYZ_person")
@allure.label("owner_email", "xyz.person@e.mail")
@allure.tag("Functional", "Form Test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Alternative Form Functionality test")
@allure.testcase("TMS_LINK-1215")
@allure.link("https://dev.example.com/", name="Website36")
@allure.issue("JIRA_LINK-6731")
@allure.description("This test is alternative - get information from data-provider class and submit form")
@allure.description_html(
    "<h1><b>This is alternative test get information from data-provider class and submit form")
class TestHomePage(BaseTestClass):
    def test_form_submission_shared_dic(self, data_set, test_logger):
        self.logger = test_logger
        self.log_info("run")
        BasePage(self.driver,self.logger).open_page(home_page_url)

        home_page = HomePage(self.driver,self.logger)
        home_page.set_name(data_set["first_name"] + " " + data_set["last_name"])
        home_page.set_email(data_set["email"])
        home_page.set_password(data_set["password"])
        home_page.check_love_ice_cream()
        home_page.shot_to("py_po_submit_form_1_" + data_set["first_name"])

        self.select_option_by_text(home_page.get_gender_dropdown(), data_set["gender"])

        home_page.submit_form()

        alert_info = home_page.get_success_message()
        home_page.shot_to("py_po_submit_form_2_" + data_set["first_name"])

        assert "Success" in alert_info
        self.log_info("end")

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def data_set(self, request):
        return request.param
