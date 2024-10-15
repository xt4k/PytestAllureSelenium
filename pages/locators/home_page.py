from selenium.webdriver.common.by import By


class HomePageLocators:
    SHOP = By.CSS_SELECTOR, "a[href='/angularpractice/shop']"
    FIELD_NAME = By.NAME, "name"#name
    EMAIL = By.NAME, "email"
    PASSWORD = By.ID, "exampleInputPassword1"
    ICE_CREAM_CHECK_BOX = By.ID, "exampleInputPassword1"

    GENDER_DROPDOWN = By.ID, "exampleFormControlSelect1"
    SUBMIT = By.XPATH, '//input[@value="Submit"]'
    SUCCESS = By.XPATH, '//div[contains(@class,"alert")]'
