import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
import time
from pages.dashboard import Dashboard
from pages.add_player import AddPlayer


class TestAddPlayer(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


    def test_add_player_only_required_fields(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        time.sleep(3)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player_button()
        time.sleep(3)
        add_player_page = AddPlayer(self.driver)
        add_player_page.title_of_page()
        add_player_page.type_in_name("Christiano")
        add_player_page.type_in_surname("Ronaldo")
        add_player_page.type_in_date_of_birth("05.02.1985")
        add_player_page.type_in_main_position("napastnik")
        add_player_page.click_on_submit_button()
        time.sleep(2)
        add_player_page.find_alert_element()
        time.sleep(3)


    @unittest.expectedFailure
    def test_negative_add_player_without_one_required_field(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        time.sleep(3)
        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_on_add_player_button()
        time.sleep(3)
        add_player_page = AddPlayer(self.driver)
        add_player_page.title_of_page()
        add_player_page.type_in_name("Christiano")
        add_player_page.type_in_surname("Ronaldo")
        add_player_page.type_in_date_of_birth("05.02.1985")
        add_player_page.click_on_submit_button()
        add_player_page.find_alert_element()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()
