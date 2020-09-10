from pages.base_page import Page
from selenium.webdriver.common.by import By


class Review(Page):

    REVIEW_TOP = (By.ID, 'tab-title-reviews')
    YOUR_REVIEW = (By.CSS_SELECTOR, 'div.description')
    STARS = (By.CSS_SELECTOR, 'a.star-5')
    REVIEW_FIELD = (By.ID, 'comment')
    NAME_FIELD = (By.ID, 'author')
    EMAIL_FIELD = (By.ID, 'email')
    SUBMIT_BTN = (By.ID, 'submit')

    REVIEWS_COUNTER = (By.CSS_SELECTOR, 'a[href="#tab-reviews"]')
    REVIEWS = (By.CSS_SELECTOR, 'ol.commentlist')

    def click_review_top(self):
        self.click(*self.REVIEW_TOP)

    def click_5_star(self):
        self.click(*self.STARS)

    def fill_out_review_form(self):
        review = self.find_element(*self.REVIEW_FIELD)
        review.clear()
        review.send_keys('Test')

        name = self.find_element(*self.NAME_FIELD)
        name.clear()
        name.send_keys('Test')

        e = self.find_element(*self.EMAIL_FIELD)
        e.clear()
        e.send_keys('test1@gmail.com')

    def click_submit(self):
        self.click(*self.SUBMIT_BTN)

    def verify_review(self):
        self.find_element(*self.YOUR_REVIEW)

    def verify_amount_reviews_macbook_air(self):
        review_counter = self.find_element(*self.REVIEWS_COUNTER).text
        assert review_counter == 'REVIEWS (0)', f'Expected REVIEWS (0), but got {review_counter}'