from pathlib import Path

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger =logger
        self.logger.info(f"[PAGE] Initializing {self.__class__.__name__} page.")

    def log_info(self, message):
            self.logger.info(f"[PAGE] {message}")

    @allure.step("Save screenshot to file: `{file_path}`")
    def shot_to(self, file_path):
        full_path = "../shots/" + file_path + ".png"
       # print(f"shot will be saved to {full_path}")
        self.log_info(f"shot will be saved to {full_path}")

        self.driver.save_screenshot(full_path)

    @allure.step("Save screenshot to file: `{file_name}`")
    def shot_attach(self, file_name):
        self.log_info(f"shot has name {file_name}")
        full_path = Path("../shots") / f"{file_name}.png"

        png_bytes = self.driver.get_screenshot_as_png()
        full_path.write_bytes(png_bytes)
        allure.attach.file(
            str(full_path),  # Ensure you're passing the full path to the screenshot
            name=f"{file_name}.png",
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Get element text")
    def get_item_name(self, element):
        return element.find_element(*BasePageLocators.ITEM_ELEMENT).text

    @allure.step('Get image path')
    def get_image_path(self, element):
        return element.find_element(*BasePageLocators.IMAGE_ELEMENT).get_attribute("src")

    @allure.step("Open page `{url}`")
    def open_page(self, url):
        self.log_info(f"Open page `{url}`")
        self.driver.get(url)
        return BasePage(self.driver,self.logger)

    @allure.step("wait for `{url}` refresh")
    def wait_refresh(self, url):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(url))
