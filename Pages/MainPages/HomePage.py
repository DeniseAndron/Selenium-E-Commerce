# test case

#load the page
#check if speakers, tablets, laptops, mice and headphones are present at the top
#check if special offer title is present
#check if the image of the special offer is present
#check if the button see offer is present and if it's working
# check the explore now button and functionality
#check the popular now title
#check the images, and view details
#check the contact us form
#follow us button if they redirect
#check go up button


import time
from selenium.webdriver.common.by import By
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/firstEcommerce")
from Pages.MainPages.BasePage import BasePage
from TestData.TestData import TestData


class HomePageTest(BasePage):
    #locators
    #images
    speakers_shop_image = (By.ID, "speakersImg")
    tablets_shop_image = (By.ID, "speakersImg")
    laptops_shop_image = (By.ID, "laptopsImg")
    mice_shop_image = (By.ID, "miceImg")
    headphones_shop_image = (By.ID,"headphonesImg")

    #links
    speakers_shop_link = (By.ID, "speakersLink")
    tablets_shop_link = (By.ID, "tabletsLink")
    laptops_shop_link = (By.ID, "laptopsLink")
    mice_shop_link = (By.ID, "miceLink")
    headphones_shop_link = (By.ID, "headphonesLink")

    #titles from the links, to confirm that we were redirected

    speakers_title = (By.LINK_TEXT, "SPEAKERS")
    tablets_title = (By.LINK_TEXT, "TABLETS")
    laptops_title = (By.LINK_TEXT, "LAPTOPS")
    mice_title = (By.LINK_TEXT, "MICE")
    headphones_title = (By.LINK_TEXT, "HEADPHONES")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def speakersLink(self):
        self.hover_to(self.speakers_shop_image)
        self.click(self.speakers_shop_link)
        self.is_visible(self.speakers_title)
        #is_displayed() method to assert if the element is displayed
        # self.driver.find_element(*self.speakers_title).is_displayed()

    def tabletsLink(self):
        self.hover_to(self.tablets_shop_image)
        self.click(self.tablets_shop_link)

    def laptopsLink(self):
        self.hover_to(self.laptops_shop_image)
        self.click(self.laptops_shop_link)

    def miceLink(self):
        self.hover_to(self.mice_shop_image)
        self.click(self.mice_shop_link)

    def headphonesLink(self):
        self.hover_to(self.headphones_shop_image)
        self.click(self.headphones_shop_link)




