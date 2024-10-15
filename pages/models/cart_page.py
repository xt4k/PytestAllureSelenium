import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators.cart_page import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):

    @allure.step("Get total amount value")
    def get_total_amount(self):
        self.log_info("Get total amount value")
        return self.driver.find_element(*CartPageLocators.TOTAL_AMOUNT).text

    @allure.step("Get prices")
    def get_prices(self):
        self.log_info("Get prices")
        return self.driver.find_elements(*CartPageLocators.PRICES)

    @allure.step("Set promo_code `{promo_code}`")
    def set_promo_code(self, promo_code):
        self.log_info(f"Set promo_code `{promo_code}`")
        self.driver.find_element(*CartPageLocators.PROMO_CODE).send_keys(promo_code)

    @allure.step("Apply promo_code")
    def apply_promo_code(self):
        self.log_info("Apply promo_code")
        self.driver.find_element(*CartPageLocators.PROMO_BUTTON).click()

    @allure.step("Get discount_percents")
    def get_discount_percent(self):
        self.log_info("Get discount_percents")
        return self.driver.find_element(*CartPageLocators.DISCOUNT_PERCENT).text[:-1]

    @allure.step("Get discount_percents sum")
    def get_sum_discounted(self):
        self.log_info("Get discount_percents sum")
        return self.driver.find_element(*CartPageLocators.SUM_DISCOUNTED).text

    @allure.step("Get promo_info")
    def get_promo_info(self):
        self.log_info("Get promo_info")
        return self.driver.find_element(*CartPageLocators.PROMO_INFO).text

    @allure.step("wait for promo_info appear")
    def wait_for_info(self):
        self.log_info("wait for promo_info appear")
        wait = (WebDriverWait(self.driver, 10))
        wait.until(expected_conditions.presence_of_element_located(*CartPageLocators.PROMO_INFO))
