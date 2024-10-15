import allure

from pages.locators.shop_page import ShopPageLocator
from pages.base_page import BasePage


class ShopPage(BasePage):

    @allure.step('Get items')
    def get_items(self):
        return self.driver.find_elements(*ShopPageLocator.SHOP_ITEMS)
