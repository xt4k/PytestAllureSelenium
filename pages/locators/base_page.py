from selenium.webdriver.common.by import By


class BasePageLocators:
    ITEM_ELEMENT = By.TAG_NAME, 'h4'
    IMAGE_ELEMENT = By.TAG_NAME, 'img'
    POSTS_SECTION = By.ID, 'posts'
    POST = By.CLASS_NAME, 'post-link'

