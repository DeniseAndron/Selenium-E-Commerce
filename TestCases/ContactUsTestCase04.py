import time
import sys
sys.path.append("C://Users/Denisa/Desktop/selenium/firstEcommerce")
from TestCases.BaseTest import TestBase
from Pages.MainPages.ContactUs import *

class ContactUsTest(TestBase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_01_title_presence(self):
        cu = ContactUsForm(self.driver)
        cu.ContactUsPressence()

    def test_02_category_dropdown(self):
        cu = ContactUsForm(self.driver)
        cu.CategoryDropdown()

    def ntest_03_product_dropdown(self):
        cu = ContactUsForm(self.driver)
        cu.ProductDropdown()

    def test_04_email_field(self):
        cu = ContactUsForm(self.driver)
        cu.EmailField()

    def test_05_send_button(self):
        cu = ContactUsForm(self.driver)
        cu.SendButton()
