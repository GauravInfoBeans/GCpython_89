import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser_name",action= "store",default="chrome")

@pytest.fixture(scope="class")
@allure.feature("test")
def setUp(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":  # add --browser_name firefox in command to run on Firefox browser
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":  # add --browser_name edge in command to run on Edge browser
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    time.sleep(2)
    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.close()