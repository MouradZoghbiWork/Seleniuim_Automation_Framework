from selenium.webdriver.common.by import By
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_text_name = "username"
        self.password_text_name = "password"
        self.login_button_xpath = "//button[@type='submit']"

    def enter_username(self, username):
        self.driver.find_element(by=By.NAME, value=self.username_text_name).clear()
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.username_text_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by=By.NAME, value=self.password_text_name).clear()
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=self.password_text_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(by=By.XPATH, value=self.login_button_xpath).click()
