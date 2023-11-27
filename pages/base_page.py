from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

from utils.settings import DEFAULT_LOCATOR_TYPE
import time


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title


    # Extra subtask
    def assert_element_text(self, driver, xpath, expected_text):
        """Comparing expected text with observed value from web element

            :param driver: webdriver instance
            :param xpath: xpath to element with text to be observed
            :param expected_text: text what we expecting to be found
            :return: None
        """
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text


    def find_element(self, driver, xpath):
        element = driver.find_element(by=By.XPATH, value=xpath)
        assert element is not None

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(3)

    def find_all_elements_by_xpath(self, driver, xpath):
        driver.find_elements(by=By.XPATH, value=xpath)

    def visibility_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((locator_type,locator)))
        time.sleep(3)

    def press_enter_on_the_element(self, selector, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(Keys.ENTER)

    def find_text_of_element(self, driver, xpath):
        element = driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        return element_text