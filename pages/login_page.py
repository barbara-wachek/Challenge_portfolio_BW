from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    remind_password_button_xpath = "//*[text()='Remind password']"
    drop_down_list_xpath = "//*[@role='button']"
    polish_language_option_xpath = "//ul/li[1]"
    english_language_option_xpath = "//*[@data-value='en']"
    header_xpath = "//h5[contains(@class, 'h5')]"
    expected_title = "Scouts panel - zaloguj"
    login_url = "https://scouts-test.futbolkolektyw.pl/pl/"


    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title

