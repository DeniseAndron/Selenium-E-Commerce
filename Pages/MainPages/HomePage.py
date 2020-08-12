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

    #menu button
    our_products_button = (By.XPATH,".//a[@translate='OUR_PRODUCTS']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def speakersLink(self):
        self.click(self.our_products_button)
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



    def laptopsLink(self):
        self.hover_to(self.laptops_shop_image)
        self.click(self.laptops_shop_link)
        self.is_visible(self.laptops_title)


    def miceLink(self):
        self.hover_to(self.mice_shop_image)
        self.click(self.mice_shop_link)
        self.is_visible(self.mice_title)


    def headphonesLink(self):
        self.hover_to(self.headphones_shop_image)
        self.click(self.headphones_shop_link)
        self.is_visible(self.headphones_title)

class SpecialOfferTest(BasePage):
    #locators
    special_menu_button = (By.XPATH, "//a[contains(text(),'SPECIAL OFFER')]")
    special_offer_image = (By.ID, "img-special-offer")
    special_offer_header = (By.LINK_TEXT, "SPECIAL OFFER")
    special_offer_button = (By.ID, "see_offer_btn")
    check_if_button_works = (By.PARTIAL_LINK_TEXT, "PRODUCT")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def imageLocated(self):
        self.is_visible(self.special_offer_image)
        self.click(self.special_menu_button)

    def headerLocated(self):
        self.is_visible(self.special_offer_header)

    def specialOfferButton(self):

        #self click it is not intercepted at a point, this is good for user testing, for now I will make another approach so that the tests pass
        # self.click(self.special_offer_button)
        self.enter_button(self.special_offer_button)
        self.is_visible(self.check_if_button_works)



# class ExploreNowSlide(BasePage):
#     #locators
#     #sliders =(By.ID, "slider-steps")
#     explore_now_text_1 = (By.XPATH, "//h2[contains(text(),'START EXPLORING HP NOTEBOOKS')]")
#     explore_now_text_2 = (By.XPATH, "//div[@class='imgSection']//h2[@class='roboto-light ng-binding'][contains(text(),'ALL YOU WANT FROM A TABLET')]")
#     explore_now_text_3 = (By.XPATH, ".//div[@class='container']//h2")
#
#     def __init__(self,driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     def imagesCarousel(self):
#         # this is not working yet////
#         self.is_visible(self.explore_now_text_1)


class PopularItemsTest(BasePage):
    #locators
    popular_menu_button = (By.XPATH, ".//a[@translate='POPULAR_ITEMS']")
    popular_article = (By.ID, 'popular_items')
    title_popular_section = (By.XPATH, ".//article[@id='popular_items']//h3")
    popular_item_1= (By.ID, 'details_16')
    popular_item_2 = (By.ID, 'details_10')
    popular_item_3 = (By.ID, 'details_21')
    check_if_buttons_work = (By.ID, 'productProperties')

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def PopularArticle(self):
        self.click(self.popular_menu_button)
        self.is_visible(self.popular_article)
        self.is_visible(self.title_popular_section)


    def PopularItemOne(self):
        self.click(self.popular_item_1)
        self.is_visible(self.check_if_buttons_work)

    def PopularItemTwo(self):
        self.click(self.popular_item_2)
        self.is_visible(self.check_if_buttons_work)

    def PopularItemThree(self):
        self.click(self.popular_item_3)
        self.is_visible(self.check_if_buttons_work)

class FollowUSTestFooter(BasePage):
    #locators
    facebook_link = (By.XPATH, ".//img[@name='follow_facebook']")
    twitter_link = (By.XPATH, ".//img[@name='follow_twitter']")
    linkedin_link = (By.XPATH, ".//img[@name='follow_linkedin']")

    facebook_redirect = (By.LINK_TEXT, "Micro Focus")
    twitter_redirect = (By.LINK_TEXT, "Micro Focus")
    linkedin_redirect = (By.PARTIAL_LINK_TEXT, "Micro Focus")

    up_button = (By.NAME, "go_up_button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# We will add later to check if the redirect url worked

    def CheckFacebook(self):
        self.click(self.facebook_link)


    def CheckTwitter(self):
        self.click(self.twitter_link)


    def CheckLinkedin(self):
        self.click(self.linkedin_link)

    def footerButton(self):
        self.is_visible(self.up_button)
        self.click(self.up_button)






