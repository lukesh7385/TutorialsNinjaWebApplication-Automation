from selenium.webdriver.common.by import By
import random
import string

class RegisterPage:
    link_Register_linkText = "Register"
    textbox_firstname_id = "input-firstname"
    textbox_lastname_name = "lastname"
    textbox_email_id = "input-email"
    textbox_phone_id = "input-telephone"
    textbox_password_id = "input-password"
    textbox_confirmPassword_xpath = "//input[@id='input-confirm']"
    radioButton_newsletter_yes_name = "newsletter"
    checkbox_privacyPolicy_name = "agree"
    button_continue_xpath = "//input[@value='Continue']"
    Button2_continue_linkText = "Continue"
    newsLetterOption_xpath = "//a[normalize-space()='Subscribe / unsubscribe to newsletter']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_register_link(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Register_linkText).click()

    def set_firstname(self, firstname):
        self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element(By.NAME, self.textbox_lastname_name).send_keys(lastname)

    def set_email(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def set_phone_no(self, phone):
        self.driver.find_element(By.ID, self.textbox_phone_id).send_keys(phone)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def set_confirm_password(self, confirm_pass):
        self.driver.find_element(By.XPATH, self.textbox_confirmPassword_xpath).send_keys(confirm_pass)

    def click_on_radiobutton_newsletter_yes(self):
        self.driver.find_element(By.NAME, self.radioButton_newsletter_yes_name).click()

    def click_on_checkbox_privacy_policy(self):
        self.driver.find_element(By.NAME, self.checkbox_privacyPolicy_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.button_continue_xpath).click()

    def click_on_continue_button2(self):
        self.driver.find_element(By.LINK_TEXT, self.Button2_continue_linkText).click()

    def clicking_on_news_letter_option(self):
        self.driver.find_element(By.XPATH, self.newsLetterOption_xpath).click()

    @staticmethod
    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

