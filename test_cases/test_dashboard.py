import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard

class TestDashboardPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_out_from_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.text_of_header()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.wait_until_sign_out_button_is_visible()
        dashboard_page.click_on_sign_out_button()
        user_login.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()