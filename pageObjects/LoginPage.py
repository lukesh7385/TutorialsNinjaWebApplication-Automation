from selenium.webdriver.common.by import By


class LoginPage:
    link_myAccount_LinkText = "My Account"
    link_login_xpath = "//a[normalize-space()='Login']"
    textbox_username_id = "input-email"
    textbox_password_id = "input-password"
    button_login_xpath = "//input[@class='btn btn-primary']"
    link_logout_LinkText = "Logout"
    button_logout_continue_linkText = "Continue"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_on_my_account(self):
        self.driver.find_element(By.LINK_TEXT, self.link_myAccount_LinkText).click()

    def click_on_login_link(self):
        self.driver.find_element(By.XPATH, self.link_login_xpath).click()

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_on_logout_link(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_LinkText).click()

    def click_on_logout_continue(self):
        self.driver.find_element(By.LINK_TEXT, self.button_logout_continue_linkText).click()