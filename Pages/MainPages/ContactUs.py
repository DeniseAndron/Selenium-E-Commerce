from selenium.webdriver.common.by import By
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/firstEcommerce")
from Pages.MainPages.BasePage import BasePage
from TestData.TestData import TestData


class ContactUsForm(BasePage):
#locators

    contact_us_title = (By.XPATH ,"//h1[@class='roboto-bold contact_us ng-scope']")
    first_drop_down = (By.NAME, "categoryListboxContactUs")

    second_drop_down = (By.NAME, "productListboxContactUs")
    email_field = (By.NAME, 'emailContactUs')
    subject_field = (By.NAME, 'subjectTextareaContactUs')
    send_button = (By.ID, 'send_btnundefined')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def ContactUsPressence(self):
        self.is_visible(self.contact_us_title)


    def CategoryDropdown(self):
        self.click(self.first_drop_down)
        self.selectItem(self.first_drop_down, TestData.category_dropdown)

    def ProductDropdown(self):
        self.click(self.second_drop_down)
        self.selectItem(self.second_drop_down, TestData.product_dropdown)

    def EmailField(self):
        self.click(self.email_field)
        self.enter_text(self.email_field,TestData.email_insert)

    def SubjectField(self):
        self.click(self.subject_field)
        self.enter_text(self.subject_field, TestData.subject_field_data)

    def SendButton(self):
        self.click(self.send_button)