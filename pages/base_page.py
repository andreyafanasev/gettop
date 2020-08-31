from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://gettop.us/'
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def assert_text(self, given_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert given_text in actual_text, f'Expected text {given_text}, but got {actual_text}'

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

