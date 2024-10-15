from selenium.webdriver.common.by import By


class PlantsCartPageLocator:
    SEARCH_TEXT = By.CLASS_NAME, "search-keyword"
    PLANTS_LIST = By.XPATH, "//div[@class='products']/div"
    PRODUCT_NAMES = By.CSS_SELECTOR, "div h4.product-name"
    PLANT_ICON = By.XPATH, "div/button"
    CART = By.CSS_SELECTOR, "a.cart-icon"
