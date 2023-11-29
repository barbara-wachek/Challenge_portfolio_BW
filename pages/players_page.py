from pages.base_page import BasePage
import time


class PlayersPage(BasePage):
    search_field_xpath = "//input"
    next_page_button_xpath = "//*[@id='pagination-next']"
    number_of_pages_xpath = "//tfoot/tr/td/div/div/div/p"
    title_of_page_xpath = "//title"
    search_first_page_kowalski_url = 'https://scouts-test.futbolkolektyw.pl/players?start=1&query=Kowalski'
    search_second_page_kowalski_url = 'https://scouts-test.futbolkolektyw.pl/players?start=2&query=Kowalski'

    def type_in_phrase(self, phrase):
        self.field_send_keys(self.search_field_xpath, phrase)

    def press_enter_on_the_search_field(self):
        self.press_enter_on_the_element(self.search_field_xpath)

    def click_on_next_page_button(self):
        self.click_on_the_element(self.next_page_button_xpath)

    def check_searching_functionality(self):
        element = self.get_current_url(self.driver)
        time.sleep(3)
        assert element == self.search_second_page_kowalski_url

