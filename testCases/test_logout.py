import time
import allure
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.LogoutPage import LogoutPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup", "log_on_failure")
@allure.severity(allure.severity_level.NORMAL)
class Test_003_Logout_Functionality:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout_functionality_001(self, setup):
        self.logger.info("*************** Logout Functionality 001 Test Start ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("**************** Login is Successful ******************")
        time.sleep(1)
        self.lp.click_on_my_account()
        self.lg = LogoutPage(self.driver)
        self.lg.click_on_logout_link()
        time.sleep(1)
        self.lg.click_on_continue_button()
        self.logger.info("************ Logout is successful *****************")
        time.sleep(1)
        self.lp.click_on_my_account()
        self.logger.info("clicking on my account")
        self.loginOption = self.driver.find_element(*LoginPage.link_login).is_displayed()
        self.logger.info("************ Verifying logout functionality 001 **************")
        if self.loginOption and self.driver.title == "Your Store":
            assert True
            self.logger.info("**************** Test Logout Functionality is Passed ****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_functionality_001.png")
            self.logger.info("************** Test Logout Functionality is Failed *******************")
            assert False
        self.logger.info("***************** End of Logout Functionality 001 ********************")
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout_functionality_002(self, setup):
        self.logger.info("*************** Logout Functionality 002 Test Start ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("**************** Login is Successful ******************")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@class='list-group-item' and contains(text(),'Logout')]").click()
        self.lg = LogoutPage(self.driver)
        self.lg.click_on_continue_button()
        self.logger.info("************ Logout is successful *****************")
        self.logger.info("************ Verifying logout functionality **************")
        self.lp.click_on_my_account()
        self.loginOption = self.driver.find_element(By.XPATH, "//a[text() = 'Login']")
        if self.loginOption.is_displayed() and self.driver.title == "Your Store":
            assert True
            self.logger.info("**************** Test Logout Functionality is Passed ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_functionality_002.png")
            self.logger.info("************** Test Logout Functionality is Failed *******************")
            self.driver.close()
            assert False
        self.logger.info("***************** End of Logout Functionality 002 ********************")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_logout_functionality_004(self, setup):
        self.logger.info("*************** Logout Functionality 004 Test Start ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("**************** Login is Successful ******************")
        time.sleep(1)
        self.lp.click_on_my_account()
        self.lg = LogoutPage(self.driver)
        self.lg.click_on_logout_link()
        time.sleep(1)
        self.driver.back()
        self.driver.refresh()
        time.sleep(1)
        self.lp.click_on_my_account()
        self.logger.info("******** Verifying Test Logout Functionality 004 ***********")
        self.loginOption = self.driver.find_element(By.LINK_TEXT, "Login").is_displayed()
        if self.loginOption:
            self.logger.info("********* Test Logout Functionality 004 is Passed **********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_functionality_004_Failed.png")
            self.logger.error("************ Test Logout Functionality 004 is Failed *************")
            assert False
        self.driver.close()
        self.logger.info("********** End Of Test Logout Functionality 004 ***************")








