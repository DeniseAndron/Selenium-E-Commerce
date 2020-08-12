import time
import sys
sys.path.append("C://Users/Denisa/Desktop/selenium/firstEcommerce")
from TestCases.BaseTest import TestBase
from Pages.MainPages.HomePage import *


class HomePageTestCase(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_speakers(self):
        hp = HomePageTopTest(self.driver)
        hp.speakersLink()

    def test_tablets(self):
        hp = HomePageTopTest(self.driver)
        hp.tabletsLink()
        self.driver.back()

    def test_laptops(self):
        hp = HomePageTopTest(self.driver)
        hp.laptopsLink()
        self.driver.back()

    def test_mice(self):
        hp = HomePageTopTest(self.driver)
        hp.miceLink()
        self.driver.back()

    def test_headphones(self):
        hp = HomePageTopTest(self.driver)
        hp.headphonesLink()
        self.driver.back()


class Special_Offer_Test(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_01_special_offer_image(self):
        so = SpecialOfferTest(self.driver)
        so.imageLocated()


    def test_02_special_offer_link(self):
        so = SpecialOfferTest(self.driver)
        so.headerLocated()

    def test_03_special_offer_button(self):
        so = SpecialOfferTest(self.driver)
        so.specialOfferButton()
        self.driver.back()

# class Explore_Now_Test(TestBase):
#
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#
#     def test_01_image_slider(self):
#         en = ExploreNowSlide(self.driver)
#         en.imagesCarousel()


class Popular_Items_Test(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_popular_article_visibility(self):
        pa = PopularItemsTest(self.driver)
        pa.PopularArticle()

    def test_popular_article_one(self):
        pa = PopularItemsTest(self.driver)
        pa.PopularItemOne()
        self.driver.back()

    def test_popular_article_two(self):
        pa = PopularItemsTest(self.driver)
        pa.PopularItemTwo()
        self.driver.back()

    def test_popular_article_three(self):
        pa = PopularItemsTest(self.driver)
        pa.PopularItemThree()
        self.driver.back()

class FollowUs_Test(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_FacebookButton(self):
        fu = FollowUSTestFooter(self.driver)
        fu.CheckFacebook()


    def test_TwitterButton(self):
        fu = FollowUSTestFooter(self.driver)
        fu.CheckTwitter()

    def test_LinkedinButton(self):
        fu = FollowUSTestFooter(self.driver)
        fu.CheckLinkedin()
