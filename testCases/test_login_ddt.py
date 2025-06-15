import time
import allure
import pytest
from pageObjects.LogoutPage import LogoutPage
from utilities import ExcelUtils
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

@pytest.mark.usefixtures("setup", "log_on_failure")
@allure.severity(allure.severity_level.CRITICAL)
class Test_002_DDT_Login:
    baseURL = ReadConfig.get_application_url()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************** Test_002_DDT_Login ***************")
        self.logger.info("************** Verifying Login Test ************")
        self.driver = setup
        self.logger.info("navigating to the url")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.get_row_count(self.path, 'Sheet1')
        print("Number of rows in a Excel: ", self.rows)
        lst_status = []  # Empty list
        for r in range(2, self.rows + 1):
            self.username = ExcelUtils.read_data(self.path, "Sheet1", r, 1)
            self.password = ExcelUtils.read_data(self.path, "Sheet1", r, 2)
            self.exp = ExcelUtils.read_data(self.path, "Sheet1", r, 3)
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
            self.lg = LogoutPage(self.driver)
            act_title = self.driver.title
            exp_title = "My Account"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed")
                    self.lp.click_on_my_account()
                    self.lg.click_on_logout_link()
                    self.lg.click_on_continue_button()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed")
                    self.lp.click_on_my_account()
                    self.lg.click_on_logout_link()
                    self.lg.click_on_continue_button()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed")
                    lst_status.append("Pass")
        print(lst_status)
        if "Fail" not in lst_status:
            self.logger.info("*********** Login DDT test passed ***********")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********** Login DDT test failed ***********")
            self.driver.close()
            assert False
        self.logger.info("****** End of the Login DDT Test *******")
        self.logger.info("******************** Completed TC_LoginDDT_002 ********************")