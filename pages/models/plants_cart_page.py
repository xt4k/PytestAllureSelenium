import allure

from pages.locators.plants_cart_page import PlantsCartPageLocator
from pages.base_page import BasePage
from pages.models.cart_popup_page import CartPopupPage


class PlantsCartPage(BasePage):

    @allure.step("Search for `{text}`")
    def text_search(self, text):
        self.log_info(f"Search for `{text}`")
        return self.driver.find_element(*PlantsCartPageLocator.SEARCH_TEXT).send_keys(text)

    @allure.step("get list of plants")
    def get_plants(self):
        self.log_info("get list of plants")
        return self.driver.find_elements(*PlantsCartPageLocator.PLANTS_LIST)

    @allure.step('get list of product names')
    def get_product_names(self):
        self.log_info('get list of product names')
        return self.driver.find_elements(*PlantsCartPageLocator.PRODUCT_NAMES)

    @allure.step("Add `{element}` to card")
    def add_to_cart(self, element):
        self.log_info(f"Add `{element}` to card")
        return element.find_element(*PlantsCartPageLocator.PLANT_ICON).click()

    @allure.step("Proceed to Card popup")
    def go_cart(self):
        self.log_info("Proceed to Card popup")
        self.driver.find_element(*PlantsCartPageLocator.CART).click()
        return CartPopupPage(self.driver,self.logger)
