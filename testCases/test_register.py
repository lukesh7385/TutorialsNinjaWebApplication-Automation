import pytest
import allure
from datetime import datetime
from selenium.webdriver.common.by import By
from pageObjects.RegisterPage import RegisterPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage

@pytest.mark.usefixtures("setup", "log_on_failure")
@allure.severity(allure.severity_level.BLOCKER)
class Test_001_Register_Functionality:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_functionality_001(self, setup):
        self.logger.info("******** Test Register Functionality 001 is Started *********")
        self.driver = setup
        self.logger.info("Navigating to the url")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("clicking on myAccount drop menu")
        self.lp.click_on_my_account()
        self.rf = RegisterPage(self.driver)
        self.logger.info("clicking on register link")
        self.rf.click_on_register_link()
        self.logger.info("*************** Providing Registration Details ***************")
        self.rf.set_firstname("Lukesh")
        self.rf.set_lastname("Ade")
        self.email = self.rf.random_generator() + "@gmail.com"
        self.rf.set_email(self.email)
        self.rf.set_phone_no("1234567890")
        self.rf.set_password("12345")
        self.rf.set_confirm_password("12345")
        self.rf.click_on_checkbox_privacy_policy()
        self.rf.click_on_continue_button()
        self.logger.info("*************** Register Functionality validation started ***************")
        exp_title = "Your Account Has Been Created!"
        if self.driver.title == exp_title:
            self.rf.click_on_continue_button2()
            exp_title = "My Account"
            if self.driver.title == exp_title:
                assert True
                self.logger.info("******* Test Register Functionality is Passed ********")
            else:
                self.logger.info("**********  Test Register Functionality 001 is Failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_001.png")
                self.driver.close()
                assert False
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_001.png")
            self.logger.info("**********  Register Functionality Test Failed **********")
            self.driver.close()
            assert False
        self.logger.info("********** End Of Test Register Functionality 001 **********")
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_functionality_002(self, setup):
        self.logger.info("******** Test Register Functionality 002 is Started *********")
        self.driver = setup
        self.logger.info("Navigating to the url")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("clicking on myAccount drop menu")
        self.lp.click_on_my_account()
        self.rf = RegisterPage(self.driver)
        self.logger.info("clicking on register link")
        self.rf.click_on_register_link()
        self.logger.info("*************** Providing Registration Details ***************")
        self.rf.set_firstname("Lukesh")
        self.rf.set_lastname("Ade")
        self.email = self.rf.random_generator() + "@gmail.com"
        self.rf.set_email(self.email)
        self.rf.set_phone_no("1234567890")
        self.rf.set_password("12345")
        self.rf.set_confirm_password("12345")
        self.rf.click_on_radiobutton_newsletter_yes()
        self.rf.click_on_checkbox_privacy_policy()
        self.rf.click_on_continue_button()
        self.logger.info("*************** Register Functionality validation started ***************")
        exp_title = "Your Account Has Been Created!"
        if self.driver.title == exp_title:
            self.rf.click_on_continue_button2()
            exp_title = "My Account"
            if self.driver.title == exp_title:
                assert True
                self.logger.info("******* Test Register Functionality is Passed ********")
            else:
                self.logger.info("**********  Test Register Functionality 002 is Failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_001.png")
                self.driver.close()
                assert False
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_001.png")
            self.logger.info("**********  Register Functionality Test Failed **********")
            self.driver.close()
            assert False
        self.driver.close()
        self.logger.info("********** End Of Test Register Functionality 002 **********")

    @pytest.mark.sanity
    def test_register_functionality_003(self, setup):
        self.logger.info("******** Test Register Functionality 002 is Started *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("clicking on myAccount drop menu")
        self.rf = RegisterPage(self.driver)
        self.rf.click_on_register_link()
        self.logger.info("clicking on register link")
        self.rf.click_on_continue_button()
        self.logger.info("clicking on continue button")
        self.logger.info("*********** Verifying Test Register Functionality 003 ***********")

        self.firstNameWarningMessages = self.driver.find_element(By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]")
        self.lastNameWarningMessages = self.driver.find_element(By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")
        self.emailWarningMessages = self.driver.find_element(By.XPATH, "//div[contains(text(),'E-Mail Address does not appear to be valid!')]")
        self.phoneWarningMessages = self.driver.find_element(By.XPATH, "//div[contains(text(),'Telephone must be between 3 and 32 characters!')]")
        self.passwordWarningMessages = self.driver.find_element(By.XPATH, "//div[contains(text(),'Password must be between 4 and 20 characters!')]")
        self.privacyPolicyWarningMessages = self.driver.find_element(By.XPATH, "//div[normalize-space()='Warning: You must agree to the Privacy Policy!']")


        warning_messages = {
                self.firstNameWarningMessages.text: "First Name must be between 1 and 32 characters!",
                self.lastNameWarningMessages.text: "Last Name must be between 1 and 32 characters!",
                self.emailWarningMessages.text: "E-Mail Address does not appear to be valid!",
                self.phoneWarningMessages.text: "Telephone must be between 3 and 32 characters!",
                self.passwordWarningMessages.text: "Password must be between 4 and 20 characters!",
                self.privacyPolicyWarningMessages.text: "Warning: You must agree to the Privacy Policy!"
            }
        print(warning_messages)
        for actual, expected in warning_messages.items():
            if actual == expected:
                assert True
                self.logger.info("Test Register Functionality 003 Passed.")
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                self.driver.save_screenshot(f".\\Screenshots\\test_register_functionality_003_failed_{timestamp}.png")
                self.logger.info(f"Actual_message: {actual} Expected_message: {expected}")
                self.logger.error(f"Test Register Functionality 003 Failed")
                assert False











