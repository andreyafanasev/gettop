from pages.base_page import Page
from pages.home_page import HomePage
from pages.quick_view import QuickView
from pages.categories_page import Categories
from pages.top_nav_menu import TopNavMenu
from pages.search_page import Search
from pages.account_page import Account
from pages.cart_page import Cart
from pages.footer_links_page import Footer
from pages.product import Product


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.page = Page(self.driver)
        self.home = HomePage(self.driver)
        self.quick = QuickView(self.driver)
        self.categories = Categories(self.driver)
        self.top = TopNavMenu(self.driver)
        self.search = Search(self.driver)
        self.account = Account(self.driver)
        self.cart = Cart(self.driver)
        self.footer = Footer(self.driver)
        self.product = Product(self.driver)