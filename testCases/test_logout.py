import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


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
        self.lp.click_on_logout_link()
        self.lp.click_on_logout_continue()
        self.logger.info("************ Logout is successful *****************")
        self.logger.info("************ Verifying logout functionality **************")
        self.lp.click_on_my_account()
        self.loginOption = self.driver.find_element(By.XPATH, "//a[text() = 'Login']")
        if self.loginOption.is_displayed() and self.driver.title == "Your Store":
            assert True
            self.logger.info("**************** Test Logout Functionality is Passed ****************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_functionality_001.png")
            self.logger.info("************** Test Logout Functionality is Failed *******************")
            self.driver.close()
            assert False
        self.logger.info("***************** End of Logout Functionality 001 ********************")

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
        self.lp.click_on_my_account()
        self.driver.find_element(By.XPATH, "//a[@class='list-group-item'][normalize-space()='Logout']").click()
        self.lp.click_on_logout_continue()
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
        self.lp.click_on_logout_link()
        self.driver.back()
        time.sleep(2)
        self.driver.refresh()
        time.sleep(2)
        self.lp.click_on_my_account()
        self.logger.info("******** Verifying Test Logout Functionality 004 ***********")

        # Verification
        try:
            # Locate the "Logout" option
            self.logoutOption = self.driver.find_element(By.XPATH, "//a[text()='Logout']")
            # Check if the "Logout" option is displayed (it shouldn't be)
            if self.logoutOption.is_displayed():
                self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_functionality_004_Failed.png")
                self.logger.error("************ Test Logout Functionality 004 is Failed *************")
                assert False
            else:
                self.logger.info("********* Test Logout Functionality 004 is Passed **********")
                assert True
        except NoSuchElementException:
            # If the element is not found, it meets the expected result
            self.logger.info("********* Test Logout Functionality 004 is Passed **********")
            assert True
        except Exception as e:
            # Handle any other exceptions gracefully
            self.logger.error(f"Test failed due to unexpected exception: {e}")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_logout_functionality_004_Error.png")
            assert False
        finally:
            self.driver.close()
            self.logger.info("********** End Of Test Logout Functionality 004 ***************")







