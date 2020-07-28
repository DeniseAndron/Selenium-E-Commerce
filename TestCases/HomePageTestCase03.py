import time
import sys
sys.path.append("C://Users/Denisa/Desktop/selenium/firstEcommerce")
from TestCases.BaseTest import TestBase
from Pages.MainPages.HomePage import *

# from TestData.TestData import TestData
#
# class HomePageTestCase(TestBase):
#
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#
#     def test_speakers(self):
#         hp = HomePageTopTest(self.driver)
#         hp.speakersLink()
#
#     def test_tablets(self):
#         hp = HomePageTopTest(self.driver)
#         hp.tabletsLink()
#
#     def test_laptops(self):
#         hp = HomePageTopTest(self.driver)
#         hp.laptopsLink()
#
#     def test_mice(self):
#         hp = HomePageTopTest(self.driver)
#         hp.miceLink()
#
#     def test_headphones(self):
#         hp = HomePageTopTest(self.driver)
#         hp.headphonesLink()


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







