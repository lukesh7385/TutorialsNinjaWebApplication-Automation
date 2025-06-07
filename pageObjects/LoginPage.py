from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    link_myAccount = (By.XPATH, "//a[@title='My Account']")
    link_login = (By.LINK_TEXT, "Login")
    textbox_username = (By.NAME, "email")
    textbox_password = (By.NAME, "password")
    button_login = (By.XPATH, "//input[@class='btn btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_my_account(self):
        try:
            link_my_account = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable(LoginPage.link_myAccount)
            )
            link_my_account.click()
            print("my account clicked successfully!")
        except Exception as e:
            print(f"Error clicking on my account: {e}")

    def click_on_login_link(self):
        try:
            login_link = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable(LoginPage.link_login)
            )
            login_link.click()
            print("Login link clicked successfully!")
        except Exception as e:
            print(f"Error clicking login link: {e}")

    def set_username(self, username):
        try:
            # Wait until the username field is visible
            username_field = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located(LoginPage.textbox_username)
            )
            username_field.send_keys(username)
            print("Username entered successfully!")
        except Exception as e:
            print(f"Error entering username: {e}")

    def set_password(self, password):
        try:
            # Wait until the password field is visible
            password_field = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.visibility_of_element_located(LoginPage.textbox_password)
            )
            password_field.send_keys(password)
            print("Password entered successfully!")
        except Exception as e:
            print(f"Error entering password: {e}")

    def click_on_login_button(self):
        try:
            # Wait for the button to be clickable
            login_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable(LoginPage.button_login)
            )
            login_button.click()
            print("Login button clicked successfully!")
        except Exception as e:
            print(f"Error clicking login button: {e}")
