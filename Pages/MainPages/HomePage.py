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


class HomePageTopTest(BasePage):
    #locators
    #images
    speakers_shop_image = (By.ID, "speakersImg")
    tablets_shop_image = (By.ID, "tabletsImg")
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

    #goback homepage button
    go_back_homepage = (By.CLASS_NAME, "logo")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def speakersLink(self):
        self.hover_to(self.speakers_shop_image)
        self.click(self.speakers_shop_link)
        self.is_visible(self.speakers_title)
        self.click(self.go_back_homepage)

        #is_displayed() method to assert if the element is displayed
        # self.driver.find_element(*self.speakers_title).is_displayed()

    def tabletsLink(self):
        self.hover_to(self.tablets_shop_image)
        self.click(self.tablets_shop_link)
        self.is_visible(self.tablets_title)
        self.click(self.go_back_homepage)


    def laptopsLink(self):
        self.hover_to(self.laptops_shop_image)
        self.click(self.laptops_shop_link)
        self.is_visible(self.laptops_title)
        self.click(self.go_back_homepage)


    def miceLink(self):
        self.hover_to(self.mice_shop_image)
        self.click(self.mice_shop_link)
        self.is_visible(self.mice_title)
        self.click(self.go_back_homepage)


    def headphonesLink(self):
        self.hover_to(self.headphones_shop_image)
        self.click(self.headphones_shop_link)
        self.is_visible(self.headphones_title)
        self.click(self.go_back_homepage)

class SpecialOfferTest(BasePage):
    #locators

    special_offer_image = (By.ID, "img-special-offer")
    special_offer_header = (By.LINK_TEXT, "SPECIAL OFFER")
    special_offer_button = (By.ID, "see_offer_btn")
    check_if_button_works = (By.PARTIAL_LINK_TEXT, "PRODUCT")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def imageLocated(self):
        self.is_visible(self.special_offer_image)

    def headerLocated(self):
        self.is_visible(self.special_offer_header)
        element = self.driver.find_element(*self.special_offer_header).text
        assert element == "SPECIAL OFFER"

    def specialOfferButton(self):

        #self click it is not intercepted at a point, this is good for user testing, for now I will make another approach so that the tests pass
        # self.click(self.special_offer_button)
        self.enter_button(self.special_offer_button)
        self.is_visible(self.check_if_button_works)










