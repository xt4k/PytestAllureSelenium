import allure
from pytest import mark

from tests.base_test_class import BaseTestClass


class TestWithMark(BaseTestClass):
    @mark.skip(reason="Feature is not implemented yet")
    @allure.epic("Web_Graphic_User_Interface")
    @allure.parent_suite("General UI Functionality")
    @allure.suite("User_Interface")
    @allure.sub_suite("Skipped test Example Sub-Suite")
    @allure.feature("Skipped test Example")
    @allure.story("Feature where Skipped test is present")
    @allure.label("owner_name", "Some Buddy")
    @allure.label("owner_email", "some.buddy@e.mail")
    @allure.tag("Functional", "Skipped Test")
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("This test will be skip")
    @allure.testcase("TMS_LINK-9985")
    @allure.link("https://dev.example.com/", name="Website178")
    @allure.issue("JIRA_LINK-9989")
    @allure.description("This test will be skip some time until feature will not be implemented")
    @allure.description_html(
        "<h1><b>This test will be skip some time until feature will not be implemented")
    def test_now_skip(self,test_logger):
        self.logger = test_logger
        self.log_info("run")
        allure.step("This test will be skip some time until feature will not be implemented")
        assert None,"Nothing here :-)"
        self.log_info("end")


    @allure.epic("Web_Graphic_User_Interface")
    @allure.parent_suite("General UI Functionality")
    @allure.suite("User_Interface")
    @allure.sub_suite("Failed test Example Sub-Suite")
    @allure.feature("Failed test Example")
    @allure.story("Feature where Failed test is present")
    @allure.label("owner_name", "Some Buddy")
    @allure.label("owner_email", "some.buddy@e.mail")
    @allure.tag("Functional", "Failed Test")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("This test will fail")
    @allure.testcase("TMS_LINK-9995")
    @allure.link("https://dev.example.com/", name="Website178")
    @allure.issue("JIRA_LINK-9999")
    @allure.description("This test will fail unconditionally - just an example of failed test")
    @allure.description_html(
        "<h1><b>This test will fail unconditionally - just an example of failed test")
    def test_always_fail(self,test_logger):
        self.logger = test_logger
        self.log_info("run")
        allure.step("This test will fail unconditionally")
        self.log_info("fail in next step")
        assert False,"Example of failed message"

    @mark.xfail(reason="Feature is deprecated")
    @allure.epic("Web_Graphic_User_Interface")
    @allure.parent_suite("General UI Functionality")
    @allure.suite("User_Interface")
    @allure.sub_suite("X-Failed test Example Sub-Suite")
    @allure.feature("X-Failed test Example")
    @allure.story("Feature where X-Failed test is present")
    @allure.label("owner_name", "Some Buddy")
    @allure.label("owner_email", "some.buddy@e.mail")
    @allure.tag("Functional", "Failed Test")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("This test will fail")
    @allure.testcase("TMS_LINK-9956")
    @allure.link("https://dev.example111.com/", name="Website148")
    @allure.issue("JIRA_LINK-9779")
    @allure.description("This test will x-fail until will not be deleted from coverage")
    @allure.description_html(
        "<h1><b>This test will x-fail until will not be deleted from coverage")
    def test_always_x_fail(self, test_logger):
        self.logger = test_logger
        self.log_info("run")
        allure.step("This test will x-fail until will not be deleted from coverage")
        self.log_info("x-fail in next step")
        assert True, "example of x-failed test"
