from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import time
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/firstEcommerce")
from Pages.MainPages.BasePage import BasePage
from TestData.TestData import TestData

class LoginPage(BasePage):
    login_icon = (By.ID, 'menuUserSVGPath')
    username_logIn = (By.XPATH, ".//div[@class='inputContainer ng-scope']//input[@name='username']")
    password_logIn = (By.XPATH, ".//div[@class='inputContainer ng-scope']//input[@name='password']")
    remember_me_check = (By.XPATH, ".//div[@class='left option ']//input[@name='remember_me']")
    login_button = (By.ID, 'sign_in_btnundefined')
    login_success_name = (By.XPATH, ".//span[@class='hi-user containMiniTitle ng-binding']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def GoToLogin(self):
        time.sleep(5)
        self.click(self.login_icon)

    def UsernameLogin(self):
        self.enter_text(self.username_logIn, TestData.loginUserName)

    def PasswordLogin(self):
        self.enter_text(self.password_logIn, TestData.loginPassword)

    def RememberButton(self):
        self.is_element_selected_Click(self.remember_me_check)

    def LoginButton(self):
        self.click(self.login_button)

    def loginError(self):
        try:
            element_success=self.driver.find_element(*self.login_success_name).text
            print("Logged in as " + element_success)

        except:
            print("You are not logged in")






