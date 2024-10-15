import allure
import pytest

from pages.base_page import BasePage
from pages.models.home_page import HomePage
from tests.base_test_class import BaseTestClass

home_page_url = "https://rahulshettyacademy.com/angularpractice/"


@allure.epic("Web_Graphic_User_Interface")
@allure.parent_suite("General UI Functionality")
@allure.suite("User_Interface")
@allure.sub_suite("Form submission availability")
@allure.feature("Form submission validation")
@allure.story("Check form submission")
@allure.label("owner_name", "XYZ_person")
@allure.label("owner_email", "xyz.person.l@e.mail")
@allure.tag("Functional", "Form Test")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Form Functionality test")
@allure.testcase("TMS_LINK-12355")
@allure.link("https://dev.example.com/", name="Website12")
@allure.issue("JIRA_LINK-6791")
@allure.description("This test get information from data-provider and submit form")
@allure.description_html(
    "<h1><b>This test get information from data-provider and submit form")
class TestHomePage(BaseTestClass):
    def test_form_submission_dic_in_file(self, data_provider,test_logger):
        self.logger = test_logger
        self.log_info("run")

        BasePage(self.driver,self.logger).open_page(home_page_url)
        home_page = HomePage(self.driver,self.logger)
        home_page.set_name(data_provider["first_name"] + " " + data_provider["last_name"])
        home_page.set_email(data_provider["email"])
        home_page.set_password(data_provider["password"])
        home_page.check_love_ice_cream()
        home_page.shot_to("py_po_submit_form_1_" + data_provider["first_name"])

        self.select_option_by_text(home_page.get_gender_dropdown(), data_provider["gender"])

        home_page.submit_form()

        alert_info = home_page.get_success_message()
        home_page.shot_to("py_po_submit_form_2_" + data_provider["first_name"])

        assert "Success" in alert_info
        self.log_info("end")

    @pytest.fixture(params=[{"first_name": "first_1", "last_name": "last_1", "email": "e@mai.l1", "password": "Password_1", "gender": "Male"},
                            {"first_name": "first_2", "last_name": "last_2", "email": "e@mai.l2","password": "Password_2", "gender": "Female"}])
    def data_provider(self, request):
        return request.param
