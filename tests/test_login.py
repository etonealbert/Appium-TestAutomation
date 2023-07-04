import unittest
from pages.login_page import LoginPage
from utilities.driver_factory import create_driver

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = create_driver()  # Assuming create_driver returns an Appium webdriver
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.enter_username('valid_username')
        self.login_page.enter_password('valid_password')
        self.login_page.click_login_button()

        # Insert an assertion here to verify successful login

    def tearDown(self):
        self.driver.quit()
