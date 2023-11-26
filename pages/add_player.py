from pages.base_page import BasePage
import time



class AddPlayer(BasePage):
    add_player_url = "https://scouts-test.futbolkolektyw.pl/en/players/add"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    age_field_xpath = "//*[@name='age']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    submit_button_xpath = "//*[@type='submit']"
    clear_button_xpath = "//span[text()='Clear']/parent::button"
    expected_title = "Add player"
    submit_alert_xpath = "//div[@role='alert']"
    expected_alert_message = "Added player."
    expected_beginning_title_of_edit_page = "Edit player"
    header_edit_xpath = "//span[contains(text(), 'Edit player')]"
    all_empty_input_fields_xpath = "//input[@value='']"

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_date_of_birth(self, date):
        self.field_send_keys(self.age_field_xpath, date)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def find_alert_element(self):
        self.find_element(self.driver, self.submit_alert_xpath)

    def click_on_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def check_emptiness_input_fields(self):
        list_of_elements = self.find_all_elements_by_xpath(self.driver, self.all_empty_input_fields_xpath)
        len(list_of_elements) == 17








