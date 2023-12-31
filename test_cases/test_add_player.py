import os
import unittest
from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from pages.login_page import LoginPage
from pages.dashboard import Dashboard
from pages.add_player import AddPlayer


class TestAddPlayer(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome()
        self.driver.get('https://dareit.futbolkolektyw.pl/pl')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)


    def test_add_player_only_required_fields(self):
        user_login = LoginPage(self.driver)
        user_login.wait_until_sign_in_button_is_visible()
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_until_sign_out_button_is_visible()
        dashboard_page.click_on_add_player_button()
        add_player_page = AddPlayer(self.driver)
        add_player_page.wait_until_submit_button_is_visible()
        add_player_page.title_of_page()
        add_player_page.type_in_name("Christiano")
        add_player_page.type_in_surname("Ronaldo")
        add_player_page.type_in_date_of_birth("05.02.1985")
        add_player_page.type_in_main_position("napastnik")
        add_player_page.click_on_submit_button()
        add_player_page.find_alert_element()



    @unittest.expectedFailure
    def test_negative_add_player_without_one_required_field(self):
        user_login = LoginPage(self.driver)
        user_login.wait_until_sign_in_button_is_visible()
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_until_sign_out_button_is_visible()
        dashboard_page.click_on_add_player_button()
        add_player_page = AddPlayer(self.driver)
        add_player_page.wait_until_submit_button_is_visible()
        add_player_page.title_of_page()
        add_player_page.type_in_name("Christiano")
        add_player_page.type_in_surname("Ronaldo")
        add_player_page.type_in_date_of_birth("05.02.1985")
        add_player_page.click_on_submit_button()
        add_player_page.find_alert_element()


    def test_add_player_clear_form_button(self):
        user_login = LoginPage(self.driver)
        user_login.wait_until_sign_in_button_is_visible()
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_until_sign_out_button_is_visible()
        dashboard_page.click_on_add_player_button()
        add_player_page = AddPlayer(self.driver)
        add_player_page.wait_until_submit_button_is_visible()
        add_player_page.title_of_page()
        add_player_page.type_in_name("Robert")
        add_player_page.type_in_surname("Lewandowski")
        add_player_page.type_in_date_of_birth("01.01.1970")
        add_player_page.type_in_main_position("napastnik")
        add_player_page.click_on_clear_button()
        add_player_page.check_emptiness_input_fields()


    # def test_add_player_with_incorrect_date(self):
    #     user_login = LoginPage(self.driver)
    #     user_login.wait_until_sign_in_button_is_visible()
    #     user_login.title_of_page()
    #     user_login.type_in_email("user01@getnada.com")
    #     user_login.type_in_password("Test-1234")
    #     user_login.click_on_sign_in_button()
    #     dashboard_page = Dashboard(self.driver)
    #     dashboard_page.wait_until_sign_out_button_is_visible()
    #     dashboard_page.click_on_add_player_button()
    #     add_player_page = AddPlayer(self.driver)
    #     add_player_page.wait_until_submit_button_is_visible()
    #     add_player_page.title_of_page()
    #     add_player_page.type_in_name("Emil")
    #     add_player_page.type_in_surname("Kwiatkowski")
    #     add_player_page.type_in_date_of_birth("01.01.2024")
    #     add_player_page.type_in_main_position("napastnik")
    #     add_player_page.click_on_submit_button()
    #     #Do poprawy metoda poniżej. Żeby test był zdany musi wyjść Fail
    #     add_player_page.check_if_player_is_added("Emil Kwiatkowski")

    def test_add_player_happy_path(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email("user01@getnada.com")
        user_login.type_in_password("Test-1234")
        user_login.click_on_sign_in_button()
        user_login.wait_until_sign_in_button_is_visible()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_until_sign_out_button_is_visible()
        dashboard_page.click_on_add_player_button()
        add_player_page = AddPlayer(self.driver)
        add_player_page.wait_until_submit_button_is_visible()
        add_player_page.title_of_page()
        add_player_page.type_in_email("test@com.pl")
        add_player_page.type_in_name("Kacper")
        add_player_page.type_in_surname("Kowalski")
        add_player_page.type_in_phone_number("666288000")
        add_player_page.type_in_weight("70")
        add_player_page.type_in_date_of_birth("12.03.1970")
        add_player_page.click_on_leg_field()
        add_player_page.click_on_right_leg()
        add_player_page.type_in_club("Real Madryt")
        add_player_page.type_in_level("XXX")
        add_player_page.type_in_main_position("napastnik")
        add_player_page.type_in_second_position("bramkarz")
        add_player_page.click_on_district()
        add_player_page.click_on_district_greater_poland()
        add_player_page.type_in_achievements("Złota Piłka")
        add_player_page.click_on_submit_button()
        add_player_page.find_alert_element()

    @classmethod
    def tearDown(self):
        self.driver.quit()
