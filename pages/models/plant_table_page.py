import allure

from pages.locators.plant_table_page import PlantTablePageLocator
from pages.base_page import BasePage


class PlantTablePage(BasePage):

    @allure.step("Select `{size}` page size")
    def select_page_size(self, size):
        self.driver.find_element(*PlantTablePageLocator.PAGE_MENU).click()
        self.driver.find_element(*PlantTablePageLocator.PAGE_MENU).send_keys(size)
        self.driver.find_element(*PlantTablePageLocator.PAGE_MENU).click()
        self.log_info(f"Select `{size}` page size")
        return self

    @allure.step('Get list of vegetables')
    def get_vegetable_list(self):
        self.log_info('Get list of vegetables')
        return self.driver.find_elements(*PlantTablePageLocator.ELEMENTS)

    @allure.step('Table sorted by name')
    def sort_table_by_name(self):
        self.log_info('Table sorted by name')
        self.driver.find_element(*PlantTablePageLocator.SORT_BY_NAME).click()
