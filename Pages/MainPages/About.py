from selenium.webdriver.common.by import By
import sys
sys.path.append("C://Users/Denisa\Desktop/selenium/firstEcommerce")
from Pages.MainPages.BasePage import BasePage


class AboutPage(BasePage):
    #locators
    menu_button = (By.ID, 'helpLink')
    #help
    menu_help_button = (By.XPATH, ".//div[@id='helpMiniTitle']/label[@translate='ABOUT']")
    check_help_redirect = (By.ID, 'aboutPage')
    #aos version
    menu_aos_button = (By.XPATH, ".//div[@id='helpMiniTitle']/label[@translate='AOS_VERSIONS']")
    version_dropdown = (By.XPATH, ".//a[@class='release_version ng-binding']")
    click_last_version = (By.XPATH, ".//label[contains(text(),'VERSION 2.5')]")

    check_whats_new = (By.ID, "whats_new_link")
    check_download = (By.ID, "downloads_link")
    check_installation = (By.ID, "installation_link")
    check_admin_client = (By.ID, "admin_client_link")
    check_docker_configuration = (By.ID, "DockerConfiguration_link")
    check_Apis = (By.ID, "APIs_link")




    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def ClickHelpButton(self):
        self.click(self.menu_button)
        self.click(self.menu_help_button)
        self.is_visible(self.check_help_redirect)

    def ClickAosVersion(self):
        self.click(self.menu_button)
        self.click(self.menu_aos_button)
        self.is_visible(self.version_dropdown)

    def CheckVersion(self):
        self.click(self.version_dropdown)
        self.click(self.click_last_version)

    def CheckLinks(self):
        self.click(self.check_whats_new)
        self.click(self.check_download)
        self.click(self.check_installation)
        self.click(self.check_admin_client)
        self.click(self.check_Apis)