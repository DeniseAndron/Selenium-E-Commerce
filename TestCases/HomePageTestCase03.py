
import sys
sys.path.append("C://Users/Denisa/Desktop/selenium/firstEcommerce")
from TestCases.BaseTest import TestBase
from Pages.MainPages.HomePage import HomePageTest
from TestData.TestData import TestData

class HomePageTestCase(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_speakers(self):
        hp = HomePageTest(self.driver)
        hp.speakersLink()

    # def test_tablets(self):
    #     hp = HomePageTest(self.driver)
    #     hp.tabletsLink()
    #
    # def test_laptops(self):
    #     hp = HomePageTest(self.driver)
    #     hp.laptopsLink()
    #
    # def test_mice(self):
    #     hp = HomePageTest(self.driver)
    #     hp.miceLink()
    #
    # def test_headphones(self):
    #     hp = HomePageTest(self.driver)
    #     hp.headphonesLink()

