import allure

from pages.base_page import BasePage
from pages.models.plant_table_page import PlantTablePage
from tests.base_test_class import BaseTestClass

unsorted_list = []
sorted_list = []
first_page = "https://rahulshettyacademy.com/seleniumPractise/#/offers"


@allure.epic("Web_Graphic_User_Interface")
@allure.parent_suite("General UI Functionality")
@allure.suite("User_Interface")
@allure.sub_suite("Table sorting availability")
@allure.feature("Sort tables validation")
@allure.story("Check table is sorted")
@allure.label("owner_name", "Ivan_Petrenko")
@allure.label("owner_email", "i.petnenko.l@e.mail")
@allure.tag("Functional", "Sorting Test")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Supplementary Functionality test")
@allure.testcase("TMS_LINK-123887")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("JIRA_LINK-447")
@allure.description("This test is navigates from home to `offers` page and then check if table may be sorted")
@allure.description_html(
    "<h1><b>This test is navigates from home to `offers` page and then check if table may be sorted")
class TestSecond(BaseTestClass):

    def test_e2e_sort_table(self, test_logger):
        self.logger = test_logger

        self.log_info("run")
        BasePage(self.driver, self.logger).open_page(first_page)

        selenium_practice_page = PlantTablePage(self.driver, self.logger)
        selenium_practice_page.select_page_size(2)

        unsorted = selenium_practice_page.get_vegetable_list()
        for item in unsorted:
            unsorted_list.append(item.text)

        selenium_practice_page.sort_table_by_name()
        sorted_name = selenium_practice_page.get_vegetable_list()
        for item in sorted_name:
            sorted_list.append(item.text)
        unsorted_list.sort()

        self.log_info("going do assertion")
        assert sorted_list == unsorted_list, "unsorted and sorted lists should be equal"
        self.log_info("end")
