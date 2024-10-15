import inspect

import pytest

import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from util.logger import Logger


@pytest.mark.usefixtures("setup")
class BaseTestClass:

    def log_info(self, action):
        current_method = inspect.currentframe().f_back.f_code.co_name
        formatted_message = "--- {} {}!----".format(current_method,action)
        self.logger.info(f"[TEST] {formatted_message}")

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def verify_element_presence(self, web_element):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(web_element))

    def select_option_by_text(self, web_element, text):
        sel = Select(web_element)
        sel.select_by_visible_text(text)

    def get_logger(self):
        return Logger.get_shared_logger("PAGE", logging.DEBUG)
