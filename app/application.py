from pages.base_page import Page
from pages.home_page import HomePage
from pages.quick_view import QuickView
from pages.categories_page import Categories


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.home = HomePage(self.driver)
        self.quick = QuickView(self.driver)
        self.categories = Categories(self.driver)


