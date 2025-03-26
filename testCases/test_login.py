import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_002_Login_Functionality:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("****************** Test_Login_001 ***************")
        self.logger.info("***************** Verifying Home Page Title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your Store":
            assert True
            self.driver.close()
            self.logger.info("************** Home page title test is passed ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title.png")
            self.driver.close()
            self.logger.error("************** Home page title test is failed ************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_functionality_001(self, setup):
        self.logger.info("************** Login test is started ************")
        self.driver = setup
        self.logger.info("navigating to the url")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("clicking on myAccount drop menu")
        self.lp.click_on_my_account()
        self.logger.info("clicking on login link")
        self.lp.click_on_login_link()
        self.logger.info("passing the username")
        self.lp.set_username(self.username)
        self.logger.info("passing the password")
        self.lp.set_password(self.password)
        self.logger.info("clicking on the login button")
        self.lp.click_on_login_button()
        time.sleep(1)
        act_title = self.driver.title
        self.logger.info("************** Verifying Login test ************")
        if act_title == "My Account":
            assert True
            self.logger.info("************** Login test is passed ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************** Login test is failed ************")
            assert False
