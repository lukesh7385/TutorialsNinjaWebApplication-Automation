import pytest
import allure
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup", "log_on_failure")
@allure.severity(allure.severity_level.CRITICAL)
class TestLoginParams:
    logger = LogGen.loggen()
    baseURL = ReadConfig.get_application_url()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_params(self, setup, data_for_login):
        self.logger.info("********** Test Login Params is Started *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Invoking browser")
        self.logger.info("Navigating to URL")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("Clicking on my account")
        self.lp.click_on_login_link()
        self.logger.info("Clicking on login link")
        self.lp.set_username(data_for_login[0])
        self.logger.info("Entering username: " + data_for_login[0])
        self.lp.set_password(data_for_login[1])
        self.logger.info("Entering password: " + data_for_login[1])
        self.lp.click_on_login_button()
        self.logger.info("Clicking on login button")
        self.logger.info("************* Verifying test_login_params *************")
        if self.driver.title == "My Account":
            if data_for_login[2] == "Pass":
                assert True
                self.logger.info("test_login_params is passed")
            else:
                self.logger.error("test_login_params is failed")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_params_failed.png")
                assert False
        else:
            if data_for_login[2] == "Fail":
                assert True
            else:
                self.logger.error("test_login_params is Failed")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login_params_failed.png")
                assert False
        self.driver.close()
        self.logger.info("test_login_params is Completed")
        self.logger.info("************* End of test_login_params *************")



