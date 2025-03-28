from selenium.webdriver.common.by import By


class LoginPage:
    link_myAccount_CSS_SELECTOR = (By.CSS_SELECTOR, "a[title='My Account']")
    link_login_PARTIAL_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Login")
    textbox_username_name = (By.NAME, "email")
    textbox_password_name = (By.NAME, "password")
    button_login_xpath = (By.XPATH, "//input[@class='btn btn-primary']")


    def __init__(self, driver):
        self.driver = driver

    def click_on_my_account(self):
        self.driver.find_element(*LoginPage.link_myAccount_CSS_SELECTOR).click()

    def click_on_login_link(self):
        self.driver.find_element(*LoginPage.link_login_PARTIAL_LINK_TEXT).click()

    def set_username(self, username):
        self.driver.find_element(*LoginPage.textbox_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*LoginPage.textbox_password_name).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*LoginPage.button_login_xpath).click()

