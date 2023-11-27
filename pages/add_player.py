from pages.base_page import BasePage
import time



class AddPlayer(BasePage):
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//span[text()='Clear']/parent::button"
    expected_title = "Add player"
    submit_alert_success_xpath = "//div[contains(@class,'toast--success')]"
    submit_alert_error_xpath = "//div[contains(@class,'toast--error')]"
    expected_alert_message = "Added player."
    expected_beginning_title_of_edit_page = "Edit player"
    header_edit_xpath = "//span[contains(text(), 'Edit player')]"
    all_input_fields_xpath = "//input[@value='']"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    leg_field_xpath = "//*[@id='mui-component-select-leg']"
    right_leg_option_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name='level']"
    second_position_field_xpath = "//*[@name='secondPosition']"
    district_field_xpath = "//*[@id='mui-component-select-district']"
    district_option_greater_poland_xpath = "//*[@id='menu-district']/div[3]/ul/li[15]"
    achievements_field_xpath = "//*[@name='achievements']"


    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)
    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone_number(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)
    def type_in_date_of_birth(self, date):
        self.field_send_keys(self.age_field_xpath, date)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def click_on_leg_field(self):
        self.click_on_the_element(self.leg_field_xpath)

    def click_on_right_leg(self):
        self.click_on_the_element(self.right_leg_option_xpath)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)
    def click_on_district(self):
        self.click_on_the_element(self.district_field_xpath)
    def click_on_district_greater_poland(self):
        self.click_on_the_element(self.district_option_greater_poland_xpath)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def find_alert_element(self):
        self.find_element(self.driver, self.submit_alert_success_xpath)

    def click_on_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def check_emptiness_input_fields(self):
        elements = self.find_all_elements_by_xpath(self.driver, self.all_input_fields_xpath)
        amount_of_input_fields = 17

        assert amount_of_input_fields == len(elements)



    def find_alert_element_not_saved(self):
        self.find_element(self.driver, self.submit_alert_error_xpath)






