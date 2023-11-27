from pages.base_page import BasePage
import re
import time


class PlayersPage(BasePage):
    search_field_xpath = "//input"
    next_page_button_xpath = "//*[@id='pagination-next']/span[1]"
    number_of_pages_xpath = "//tfoot/tr/td/div/div/div/p"

    def type_in_phrase(self, phrase):
        self.field_send_keys(self.search_field_xpath, phrase)

    def press_enter_on_the_search_field(self):
        self.press_enter_on_the_element(self.search_field_xpath)

    def click_on_next_page_button(self):
        self.click_on_the_element(self.next_page_button_xpath)

    def check_text_of_searching_button(self):
        return self.find_text_of_element(self.driver, self.number_of_pages_xpath)

    def check_searching_functionality(self):
        element_1 = re.search(r"\d+$", self.check_text_of_searching_button()).group(0)
        time.sleep(2)
        self.click_on_next_page_button()
        time.sleep(2)
        element_2 = re.search(r"\d+$", self.check_text_of_searching_button()).group(0)
        assert element_1 == element_2
