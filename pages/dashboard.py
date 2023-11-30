from pages.base_page import BasePage

class Dashboard(BasePage):
    main_page_xpath = "//*[text()='Strona główna' or text()='Main page']"
    players_xpath = "//*[text()='Gracze' or text()='Players']"
    language_xpath = "//ul[contains(@class, 'padding')][2]/div[1]"
    sign_out_xpath = "//ul[contains(@class, 'padding')][2]/div[2]"
    dev_team_contact_button_xpath = "//a[contains(@class, 'MuiButtonBase')]"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button"
    last_created_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button"
    last_updated_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button"
    last_created_match_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button"
    last_updated_match_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button"
    last_updated_report_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button"
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/pl/"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.dev_team_contact_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_sign_out_button(self):
        self.click_on_the_element(self.sign_out_xpath)

    def wait_until_sign_out_button_is_visible(self):
        self.visibility_of_element_located(self.sign_out_xpath)

    def click_on_players_section(self):
        self.click_on_the_element(self.players_xpath)
