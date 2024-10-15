from selenium.webdriver.common.by import By


class CartPageLocators:
    TOTAL_AMOUNT = By.CSS_SELECTOR, ".totAmt"
    PRICES = By.CSS_SELECTOR, "tr td:nth-child(5) p"

    PROMO_CODE = By.CLASS_NAME, "promoCode"
    PROMO_BUTTON = By.CLASS_NAME, "promoBtn"
    PROMO_INFO = By.CLASS_NAME, "promoInfo"

    DISCOUNT_PERCENT= By.CSS_SELECTOR, ".discountPerc"
    SUM_DISCOUNTED = By.CSS_SELECTOR, ".discountAmt"
