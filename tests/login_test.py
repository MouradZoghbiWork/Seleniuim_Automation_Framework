import allure
import pytest

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils import utils
import moment

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            # home page
            driver = self.driver
            home = HomePage(driver)
            home.click_welcome_link()
            home.click_logout_link()
            x = driver.title
            assert x == 'abc' # OrangeHRM
        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            current_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = test_name + "_" + current_time
            # allure.attach.file("reports",
            #                    name=screenshot_name,
            #                    attachment_type=allure.attachment_type.PNG)
            allure.attach(self.driver.get_screen_shot_as_png,
                          name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("Exception occured")
            current_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            test_name = utils.whoami()
            screenshot_name = test_name + "_" + current_time
            # allure.attach.file("reports",
            #                    name=screenshot_name,
            #                    attachment_type=allure.attachment_type.PNG)
            allure.attach(self.driver.get_screen_shot_as_png,
                          name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            # to save screen shot as file
            driver.get_screenshot_as_file("C:/Users/moura/PycharmProjects/udemy/Automation_Framework/screenshots/"
                                          + screenshot_name
                                          + ".png",
                                          )
            raise
        else:
            print("No exception error ")
        finally:
            print("I am in finally bloc")

