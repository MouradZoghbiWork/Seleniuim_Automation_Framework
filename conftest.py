from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type browser name chrome or firefox")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        # https://github.com/SergeyPirogov/webdriver_manager
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == 'firefox':
        # https://github.com/SergeyPirogov/webdriver_manager
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")
