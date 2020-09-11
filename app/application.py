from pages.base_page import Page
from pages.home_page import HomePage
from pages.quick_view import QuickView
from pages.categories_page import Categories
from pages.top_nav_menu import TopNavMenu
from pages.search_page import Search
from pages.account_page import Account
from pages.cart_page import Cart
from pages.footer_links_page import Footer
from pages.product_page import Product
from pages.social_links_page import SocialLinks
from pages.adding_to_cart_page import AddingToCart
from pages.out_of_stock_page import OutOfStock
from pages.you_may_also_like_page import YouMayAlsoLike
from pages.description_page import Description
from pages.reviews_page import Review
from pages.category_page import Category


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
        self.sl = SocialLinks(self.driver)
        self.add = AddingToCart(self.driver)
        self.out = OutOfStock(self.driver)
        self.you = YouMayAlsoLike(self.driver)
        self.des = Description(self.driver)
        self.review = Review(self.driver)
        self.cat = Category(self.driver)