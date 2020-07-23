import unittest
import HtmlTestRunner
from selenium import webdriver
import time
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/firstEcommerce")


from TestData.TestData import TestData
from drivers.Drivers import executables

class TestBase(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        #disable the pop-up notifications
        chrome_options.add_argument("--disable-notifications")

        cls.driver = webdriver.Chrome(executables.CHROME_EXECUTABLE_PATH, options=chrome_options)
        cls.driver.get(TestData.baseURL)
        cls.driver.maximize_window()
        assert "Advantage Shopping" in cls.driver.title


    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.delete_all_cookies()
    #     cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner (output="C:\\Users\\Denisa\\Desktop\\selenium\\facebook\\reports"))