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
                self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_002.png")
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
    @pytest.mark.regression
    def test_register_functionality_003(self, setup):
        self.logger.info("******** Test Register Functionality 003 is Started *********")
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

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_functionality_004(self, setup):
        self.logger.info("******** Test Register Functionality 004 is Started *********")
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
                self.rf.clicking_on_news_letter_option()
                if self.driver.find_element(By.XPATH, "//input[@value='1']").is_selected():
                    self.driver.find_element(By.XPATH, "//div[@class='pull-right']").click()
                    success_message = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
                    if success_message == "Success: Your newsletter subscription has been successfully updated!":
                        assert True
                        self.logger.info("******* Test Register Functionality 004 is Passed ********")
                    else:
                        self.logger.info("******* Test Register Functionality 004 is Failed ********")
                        self.driver.save_screenshot(".\\Screenshots\\test_register_functionality_004_failed.png")
                        assert False
                else:
                    self.logger.info("******* Test Register Functionality 004 is Failed ********")
                    self.driver.save_screenshot(".\\Screenshots\\test_register_functionality_004_failed.png")
                    assert False
            else:
                self.logger.info("**********  Test Register Functionality 004 is Failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_001.png")
                self.driver.close()
                assert False

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_004_failed.png")
            self.logger.info("**********  Test Register Functionality 004 Failed **********")
            self.driver.close()
            assert False
        self.driver.close()
        self.logger.info("********** End Of Test Register Functionality 004 **********")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_functionality_005(self, setup):
        self.logger.info("******** Test Register Functionality 005 is Started *********")
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
                self.rf.clicking_on_news_letter_option()
                if self.driver.find_element(By.XPATH, "//input[@value='0']").is_selected():
                    self.driver.find_element(By.XPATH, "//div[@class='pull-right']").click()
                    success_message = self.driver.find_element(By.XPATH,
                                                               "//div[@class='alert alert-success alert-dismissible']").text
                    if success_message == "Success: Your newsletter subscription has been successfully updated!":
                        assert True
                        self.logger.info("******* Test Register Functionality 005 is Passed ********")
                    else:
                        self.logger.info("******* Test Register Functionality 005 is Failed ********")
                        self.driver.save_screenshot(".\\Screenshots\\test_register_functionality_005_failed.png")
                        assert False
                else:
                    self.logger.info("******* Test Register Functionality 004 is Failed ********")
                    self.driver.save_screenshot(".\\Screenshots\\test_register_functionality_005_failed.png")
                    assert False
            else:
                self.logger.info("**********  Test Register Functionality 005 is Failed **********")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_005.png")
                self.driver.close()
                assert False

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_005_failed.png")
            self.logger.info("**********  Test Register Functionality 005 Failed **********")
            self.driver.close()
            assert False
        self.driver.close()
        self.logger.info("********** End Of Test Register Functionality 005 **********")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_register_functionality_006(self, setup):
        self.logger.info("******** Test Register Functionality 006 is Started *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("clicking on myAccount drop menu")
        self.rf = RegisterPage(self.driver)
        self.rf.click_on_register_link()
        self.logger.info("clicking on register link")
        self.logger.info("*************** Verifying Register Functionality 006  ***************")
        if self.driver.title == "Register Account":
            self.lp.click_on_my_account()
            self.lp.click_on_login_link()
            self.driver.find_element(By.XPATH, "//a[normalize-space()='Continue']").click()
            if self.driver.title == "Register Account":
                self.lp.click_on_my_account()
                self.lp.click_on_login_link()
                self.rf.click_on_right_column_register_link()
                if self.driver.title == "Register Account":
                    self.logger.info("**********  Test Register Functionality 006 Failed **********")
                    assert True
                else:
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_006_failed.png")
                    self.logger.info("**********  Test Register Functionality 006 Failed **********")
                    self.driver.close()
                    assert False
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_006_failed.png")
                self.logger.info("**********  Test Register Functionality 006 Failed **********")
                self.driver.close()
                assert False

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_register_functionality_006_failed.png")
            self.logger.info("**********  Test Register Functionality 006 Failed **********")
            self.driver.close()
            assert False
        self.driver.close()
        self.logger.info("********** End Of Test Register Functionality 006 **********")















