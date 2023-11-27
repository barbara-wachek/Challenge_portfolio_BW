import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
import time
from pages.dashboard import Dashboard


class TestLoginPage(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/pl')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.text_of_header()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    def test_log_in_to_the_system_with_incorrect_password(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("1234")
        user_login.click_on_sign_in_button()
        user_login.invalid_password_message()
        time.sleep(5)

    def test_select_english(self):
        user_login = LoginPage(self.driver)
        user_login.select_language("english")
        user_login.check_chosen_language("english")

    def test_select_polish(self):
        user_login = LoginPage(self.driver)
        user_login.select_language("polski")
        user_login.check_chosen_language("polski")

    def test_change_language(self):
        user_login = LoginPage(self.driver)
        user_login.select_language("english")
        time.sleep(2)
        user_login.select_language("polski")
        time.sleep(2)
        user_login.check_chosen_language("polski")


    @classmethod
    def tearDown(self):
        self.driver.quit()



