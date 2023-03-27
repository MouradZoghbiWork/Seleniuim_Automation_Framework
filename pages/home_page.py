from selenium.webdriver.common.by import By
import time


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_xpath = "//div[@class='oxd-topbar-header-userarea']"
        self.logout_button_partial_link = "Logout"

    def click_welcome_link(self):
        self.driver.find_element(by=By.XPATH, value=self.welcome_link_xpath).click()
        time.sleep(1)

    def click_logout_link(self):
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=self.logout_button_partial_link).click()
        time.sleep(1)

