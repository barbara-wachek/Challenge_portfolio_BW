import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.players_page import PlayersPage



class TestPlayersPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://dareit.futbolkolektyw.pl/pl')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


    def test_search_player_by_surname(self):
        user_login = LoginPage(self.driver)
        user_login.wait_until_sign_in_button_is_visible()
        user_login.title_of_page()
        user_login.text_of_header()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_until_sign_out_button_is_visible()
        dashboard_page.click_on_players_section()
        players_page = PlayersPage(self.driver)
        players_page.type_in_phrase("Kowalski")
        players_page.press_enter_on_the_search_field()
        players_page.click_on_next_page_button()
        players_page.check_searching_functionality()


    @classmethod
    def tearDown(self):
        self.driver.quit()
