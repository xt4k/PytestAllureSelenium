import allure

from pages.locators.cart_popup_page import CartPopupPageLocators
from pages.base_page import BasePage
from pages.models.cart_page import CartPage


class CartPopupPage(BasePage):

    @allure.step('Proceed to checkout')
    def proceed_to_checkout(self):
        self.log_info("Proceed to checkout")
        self.driver.find_element(*CartPopupPageLocators.PROCEED_CHECKOUT).click()
        return CartPage(self.driver, self.logger)
