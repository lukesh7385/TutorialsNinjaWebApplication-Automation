import allure
import pytest
from selenium.webdriver.common.by import By
from pageObjects.ForgotPasswordPage import ForgotPasswordPage
from pageObjects.LoginPage import LoginPage
from pageObjects.RegisterPage import RegisterPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup", "log_on_failure")
@allure.severity(allure.severity_level.CRITICAL)
class Test_004_Forgot_Password:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_forgot_password_001(self, setup):
        self.driver = setup
        self.logger.info("************ Test Forgot Password 001 Start ************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("clicking on my account")
        self.lp.click_on_login_link()
        self.logger.info("clicking on login link")
        self.fp = ForgotPasswordPage(self.driver)
        self.fp.clicking_on_forgot_password_link()
        self.logger.info("clicking on forgot password link")
        self.rp = RegisterPage(self.driver)
        self.fp.set_email(self.rp.random_generator() + "@gmail.com")
        self.logger.info("Entering the non existing email")
        self.fp.clicking_on_continue_button()
        self.warningMessage = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
        if self.warningMessage == "Warning: The E-Mail Address was not found in our records, please try again!":
            assert True
            self.logger.info("************* Test Forgot Password 001 Passed ***************")
            self.logger.info(f"{self.warningMessage}")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_forgot_password_001_failed.png")
            self.logger.info("************* Test Forgot Password 001 Failed ***************")
            self.logger.info(f"{self.warningMessage}")
            assert False
        self.driver.quit()
        self.logger.info("*************** End of Test Forgot Password 001 *****************")

    @pytest.mark.sanity
    def test_forgot_password_002(self, setup):
        self.driver = setup
        self.logger.info("************ Test Forgot Password 002 Start ************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("clicking on my account")
        self.lp.click_on_login_link()
        self.logger.info("clicking on login link")
        self.fp = ForgotPasswordPage(self.driver)
        self.fp.clicking_on_forgot_password_link()
        self.logger.info("clicking on forgot password link")
        self.rp = RegisterPage(self.driver)
        self.fp.clicking_on_continue_button()
        assert False

    @pytest.mark.sanity
    def test_forgot_password_003(self, setup):
        self.driver = setup
        self.logger.info("************ Test Forgot Password 003 Start ************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("clicking on my account")
        self.lp.click_on_login_link()
        self.logger.info("clicking on login link")
        self.fp = ForgotPasswordPage(self.driver)
        self.fp.clicking_on_forgot_password_link()
        self.logger.info("clicking on forgot password link")
        self.logger.info("************ Verifying Test Forgot Password 003 ************")
        self.placeholderText = self.driver.find_element(By.XPATH, "// input[ @ id = 'input-email']").get_attribute('placeholder')
        if self.placeholderText == "E-Mail Address":
            self.logger.info(self.placeholderText)
            assert True
            self.logger.info("*********** Test Forgot Password 003 Passed *************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_forgot_password_003_failed.png")
            self.logger.error("*********** Test Forgot Password 003 Failed *************")
            assert False
        self.driver.quit()
        self.logger.info("************** End of Test Forgot Password 003 ********************")

    @pytest.mark.sanity
    def test_forgot_password_004(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Forgot Password 004 Is Start *****************")
        try:
            self.driver.get(self.baseURL)
            self.lp = LoginPage(self.driver)
            self.lp.click_on_my_account()
            self.logger.info("clicking on my account")
            self.lp.click_on_login_link()
            self.logger.info("clicking on login link")
            self.fp = ForgotPasswordPage(self.driver)
            self.fp.clicking_on_forgot_password_link()
            self.logger.info("clicking on forgot password link")
            self.fp.clicking_on_continue_button()
            self.logger.info("Clicking on continue button")
            self.logger.info("************* Verifying Test Forgot Password 004 **************")
            self.error_message = self.driver.find_element(By.XPATH, "//p[contains(text(),'Enter the e-mail address associated with your acco')]")
            if "Enter the e-mail address associated with your account" in self.error_message.text:
                assert True
                self.logger.info("*********** Test Forgot Password 004 Is Passed *********")
            else:
                print("No error message displayed for the empty 'E-Mail Address' field.")
                self.logger.info("*********** Test Forgot Password 004 Is Failed ************")
                assert False
        finally:
                self.driver.quit()










