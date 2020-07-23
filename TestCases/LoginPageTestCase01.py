import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/firstEcommerce")
from TestCases.BaseTest import TestBase
from Pages.MainPages.Login import LoginPage
from TestData.TestData import TestData

class LoginPageTestCase(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_01_LoginProfile(self):
        lp = LoginPage(self.driver)
        lp.GoToLogin()

    def test_02_TypeLoginUsername(self):
        lp = LoginPage(self.driver)
        lp.UsernameLogin()

    def test_03_TypeLoginPassword(self):
        lp = LoginPage(self.driver)
        lp.PasswordLogin()

    def test_04_RememberMeButton(self):
        lp = LoginPage(self.driver)
        lp.RememberButton()





