import logging

import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from util.logger import Logger

driver = None

default_home_page = "https://rahulshettyacademy.com/angularpractice/shop"

#
# @mark.skip
# @fixture(scope='session')
# def chrome_browser():
#     browser = webdriver.Chrome()
#     yield browser
#
#     #Tear down browser
#     print("I am tearing down browser")
#     #return  browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="define: chrome or firefox"
    )
    parser.addoption(
        "--home_page", action="store", default=default_home_page, help="set home_page"
    )


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function", autouse=True)
def test_logger():
    logger = Logger.get_shared_logger("TEST", logging.DEBUG)
    logger.info("---started logging!---")
    yield logger
    logger.info("---finished logging!---")


@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("--browser_name")
    home_page = request.config.getoption("--home_page")

    print(f"----- selected browser:`{browser_name}` --------.")
    print(f"----- home_page:`{home_page}` --------.")

    if browser_name == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
       # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--window-size=1920,1080")

        service_obj = ChromeService("c:\\programs\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")

        service_obj = webdriver.FirefoxService(log_output='gecko.log', service_args=['--log', 'debug'])
        driver = webdriver.Firefox(service=service_obj, options=options)
    else:
        AssertionError("browser is undefined")

    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.quit()

