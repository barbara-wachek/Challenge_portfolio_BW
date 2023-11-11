from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//*[@type='submit']"
    remind_password_button_xpath = "//*[text()='Remind password']"
    drop_down_list_xpath = "//*[@role='button']"
    polish_language_option_xpath = "//ul/li[1]"
    english_language_option_xpath = "//*[@data-value='en']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
