from selenium.webdriver.common.by import By


class ForgotPasswordPage:
    link_forgotPassword_xpath = (By.XPATH, "//div[@class='form-group']//a[normalize-space()='Forgotten Password']")
    inputTextBox_emailAddress_xpath = (By.XPATH, "//input[@id='input-email']")
    button_continue_xpath = (By.XPATH, "//input[@value='Continue']")



    def __init__(self, driver):
        self.driver = driver

    def clicking_on_forgot_password_link(self):
        self.driver.find_element(*ForgotPasswordPage.link_forgotPassword_xpath).click()

    def set_email(self, email):
        self.driver.find_element(*ForgotPasswordPage.inputTextBox_emailAddress_xpath).send_keys(email)

    def clicking_on_continue_button(self):
        self.driver.find_element(*ForgotPasswordPage.button_continue_xpath).click()

