from selenium.webdriver.common.by import By

class PlantTablePageLocator:
    PAGE_MENU = (By.ID, "page-menu")
    ELEMENTS = By.XPATH, "//tr/td[1]"
    SORT_BY_NAME= By.XPATH, "//span[text()='Veg/fruit name']"
