import sys
sys.path.append("C://Users/Denisa/Desktop/selenium/firstEcommerce")
from TestCases.BaseTest import TestBase
from Pages.MainPages.About import *


class About_Page_Test(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_01_NavigateHelp(self):
        ap = AboutPage(self.driver)
        ap.ClickHelpButton()

    def test_02_NavigateAOS(self):
        ap = AboutPage(self.driver)
        ap.ClickAosVersion()

    def test_03_VersionDropDown(self):
        ap = AboutPage(self.driver)
        ap.CheckVersion()

    def test_04_LeftMenuLinks(self):
        ap = AboutPage(self.driver)
        ap.CheckLinks()

