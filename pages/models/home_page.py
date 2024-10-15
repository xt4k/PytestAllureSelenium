import allure

from pages.locators.home_page import HomePageLocators
from pages.base_page import BasePage
from pages.models.shop_page import ShopPage


class HomePage(BasePage):

    @allure.step('Click to shop button')
    def shop_button(self):
        self.driver.find_element(*HomePageLocators.SHOP).click()
        self.log_info("click shop btn")
        return ShopPage(self.driver, self.logger)

    @allure.step('Set name: "{text} and send it')
    def set_name(self, text):
        self.log_info('Click to shop button')
        self.driver.find_element(*HomePageLocators.FIELD_NAME).send_keys(text)
        return HomePage(self.driver,self.logger)

    @allure.step("Set email: '{text}'")
    def set_email(self, text):
        self.log_info("Set email: '{text}'")
        self.driver.find_element(*HomePageLocators.EMAIL).send_keys(text)
        return HomePage(self.driver,self.logger)

    @allure.step("Set password: `{text}`")
    def set_password(self, text):
        self.log_info("Set password: `{text}`")
        self.driver.find_element(*HomePageLocators.PASSWORD).send_keys(text)
        return HomePage(self.driver,self.logger)

    @allure.step('Click to ice-cream element')
    def check_love_ice_cream(self):
        self.log_info('Click to ice-cream element')
        self.driver.find_element(*HomePageLocators.ICE_CREAM_CHECK_BOX).click()
        return HomePage(self.driver,self.logger)

    @allure.step('Submit form')
    def submit_form(self):
        self.log_info('Submit form')
        self.driver.find_element(*HomePageLocators.SUBMIT).click()
        return HomePage(self.driver,self.logger)

    @allure.step('Get success message text')
    def get_success_message(self):
        self.log_info('Get success message text')
        return self.driver.find_element(*HomePageLocators.SUCCESS).text

    @allure.step('Get gender dropdown element')
    def get_gender_dropdown(self):
        self.log_info('Get gender dropdown element')
        return self.driver.find_element(*HomePageLocators.GENDER_DROPDOWN)
