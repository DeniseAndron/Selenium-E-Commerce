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
    remember_me_check = (By.CLASS_NAME, 'ng-pristine ng-untouched ng-valid')
    login_button = (By.ID, 'sign_in_btnundefined')


    def __init__(self, driver):
        self.driver = driver

    def GoToLogin(self):
        time.sleep(5)
        self.click(self.login_icon)

    def UsernameLogin(self):
        self.enter_text(self.username_logIn, TestData.loginUserName)

    def PasswordLogin(self):
        self.enter_text(self.password_logIn, TestData.loginPassword)

    def RememberButton(self):
        self.is_enabled(self.remember_me_check)

