from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SocialLinks(Page):

    FB_LNK = (By.CSS_SELECTOR, 'a.button.facebook')
    TW_LNK = (By.CSS_SELECTOR, 'a.button.twitter')
    EMAIL_LNK = (By.CSS_SELECTOR, 'a.button.email')
    PINT_LNK = (By.CSS_SELECTOR, 'a.button.pinterest')
    LINKEDIN_LNK = (By.CSS_SELECTOR, 'a.button.linkedin')

    def click_fb_link(self):
        self.click(*self.FB_LNK)

    def click_twitter_link(self):
        self.click(*self.TW_LNK)

    def click_email_link(self):
        self.click(*self.EMAIL_LNK)

    def click_pinterest_link(self):
        self.click(*self.PINT_LNK)

    def click_linkedin_link(self):
        self.click(*self.LINKEDIN_LNK)

    def verify_fb_page(self):
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'facebook.com' in self.driver.current_url, f'Expected Facebook page, but got {self.driver.current_url}'

    def verify_twitter_page(self):
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'twitter.com' in self.driver.current_url, f'Expected Twitter page, but got {self.driver.current_url}'

    def verify_email_page(self):
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'google.com' in self.driver.current_url, f'Expected Google page, but got {self.driver.current_url}'

    def verify_pinterest_page(self):
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'pinterest.com' in self.driver.current_url, f'Expected Pinterest page, but got {self.driver.current_url}'

    def verify_linkedin_page(self):
        self.driver.wait.until(EC.new_window_is_opened)
        current_windows = self.driver.window_handles
        self.driver.switch_to_window(current_windows[1])
        assert 'linkedin.com' in self.driver.current_url, f'Expected LinkedIn page, but got {self.driver.current_url}'