import re
# from selenium import webdriver
# # pip install webdriver-manager
# from webdriver_manager.chrome import ChromeDriverManager
from library.reading_excel import *
from library.config import Config
from library.generic_lib import Generic


class Register(Generic):

    def __init__(self, value):
        self.locator = read_locators(Config.REG_PAGE_OBJECTS)
        self.driver = value
        super().__init__(value)

    def sign_up_link(self):
        # loc_name, loc_value = self.locator["register_link"]
        # self.driver.find_element(loc_name, loc_value).click()

        self.click_on_element(self.locator["sign_up"])

    def scrollpage(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


    def register_new_user_link(self):
        # loc_name, loc_value = self.locator["register_link"]
        # self.driver.find_element(loc_name, loc_value).click()

        self.click_on_element(self.locator["register_new"])


    def enter_firstname(self, firstname):
        self.enter_text(self.locator["fname"], value=firstname)


    def enter_lastname(self, lastname):
        self.enter_text(self.locator["lname"], value=lastname)

    def enter_email(self, email):
        self.enter_text(self.locator["email_txtfield"], value=email)

    def enter_password(self, pwd1):
        self.enter_text(self.locator["password"], value=pwd1)

    def click_checkbox(self):
        self.click_on_element(self.locator["checkbox"])


    def click_reg_btn(self):
        self.click_on_element(self.locator["submit"])

    def captcha_handle(self):
        self.click_on_element(self.locator["handle_captcha"])