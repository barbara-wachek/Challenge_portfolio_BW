from pages.base_page import BasePage
import time


class PlayersPage(BasePage):
    search_field_xpath = "//input"
    next_page_button_xpath = "//*[@id='pagination-next']"
    number_of_pages_xpath = "//tfoot/tr/td/div/div/div/p"

    def type_in_phrase(self, phrase):
        self.field_send_keys(self.search_field_xpath, phrase)

    def press_enter_on_the_search_field(self):
        self.press_enter_on_the_element(self.search_field_xpath)

    def click_on_next_page_button(self):
        self.click_on_the_element(self.next_page_button_xpath)

    # def check_searching_functionality(self):
    #     element_1 = re.findall(r"\d+$", self.check_number_of_searching_pages())
    #     time.sleep(2)
    #     self.click_on_next_page_button()
    #     time.sleep(2)
    #     element_2 = re.findall(r"\d+$", self.check_number_of_searching_pages())
    #     assert element_1 == element_2

    def check_searching_functionality(self):
        element_1 = self.check_text_of_element(self.driver, self.number_of_pages_xpath)
        time.sleep(3)
        self.click_on_next_page_button()
        time.sleep(3)
        element_2 = self.check_text_of_element(self.driver, self.number_of_pages_xpath)
        time.sleep(3)
        assert element_1[-5:-1] + element_1[-1:] == element_2[-5:-1] + element_2[-1:]

