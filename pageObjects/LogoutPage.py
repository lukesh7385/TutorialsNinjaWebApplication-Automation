from selenium.webdriver.common.by import By


class LogoutPage:
    link_logout_LinkText = (By.LINK_TEXT, "Logout")
    button_logout_continue_linkText = (By.LINK_TEXT, "Continue")


    def __init__(self, driver):
        self.driver = driver

    def click_on_logout_link(self):
        self.driver.find_element(*LogoutPage.link_logout_LinkText).click()

    def click_on_continue_button(self):
        self.driver.find_element(*LogoutPage.button_logout_continue_linkText).click()
