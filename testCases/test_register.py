import random
import string
import pytest
import allure
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
        self.email = random_generator() + "@gmail.com"
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
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))









