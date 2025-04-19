import allure
import pytest
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchPage import SearchPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures('setup', 'log_on_failure')
@allure.severity(allure.severity_level.CRITICAL)
class Test_005_Search_Functionality:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_search_functionality_001(self, setup):
        self.driver = setup
        self.logger.info("**************** Test Search Functionality 001 Started ******************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the URL")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Searching iMac")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")

        self.logger.info("*********** Verifying Test Search functionality 001 ************")
        self.result = self.driver.find_element(By.LINK_TEXT, "iMac").text
        if self.result == "iMac":
            self.logger.info(f"{self.result}")
            assert True
            self.logger.info("********** Test Search Functionality 001 is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_search_functionality_001_failed.png")
            self.logger.error("********** Test Search Functionality 001 is Failed ***********")
            assert False
        self.logger.info("***************** End Of Test Search Functionality 001 ******************")
        self.driver.quit()

    @pytest.mark.sanity
    def test_search_functionality_002(self, setup):
        self.driver = setup
        self.logger.info("**************** Test Search Functionality 002 Started ******************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the URL")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("Fitbit")
        self.logger.info("Searching Fitbit")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")

        self.logger.info("*********** Verifying Test Search functionality 002 ************")
        self.actMessage = self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches "
                                                             "the search criter')]").text
        if self.actMessage == "There is no product that matches the search criteria.":
            assert True
            self.logger.info("********** Test Search Functionality 002 is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_search_functionality_002_failed.png")
            self.logger.error("********** Test Search Functionality 002 is Failed ***********")
            assert False
        self.logger.info("***************** End Of Test Search Functionality 002 ******************")
        self.driver.quit()

    @pytest.mark.sanity
    def test_search_functionality_003(self, setup):
        self.driver = setup
        self.logger.info("**************** Test Search Functionality 003 Started ******************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the URL")
        self.sf = SearchPage(self.driver)
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.logger.info("*********** Verifying Test Search functionality 003 ************")
        self.actMessage = self.driver.find_element(By.XPATH, "//p[contains(text(),'There is no product that matches "
                                                             "the search criter')]").text
        if self.actMessage == "There is no product that matches the search criteria.":
            assert True
            self.logger.info("********** Test Search Functionality 003 is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_search_functionality_003_failed.png")
            self.logger.error("********** Test Search Functionality 003 is Failed ***********")
            assert False
        self.logger.info("***************** End Of Test Search Functionality 003 ******************")
        self.driver.quit()

    @pytest.mark.sanity
    def test_search_functionality_004(self, setup):
        self.driver = setup
        self.logger.info("**************** Test Search Functionality 004 Start ****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the URL")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("***************** Login is Successful *********************")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.sf.click_on_search_button()
        self.logger.info("****************** Verifying Test Search Functionality 004 ***************")
        self.result = self.driver.find_element(By.LINK_TEXT, "iMac").text
        if self.result == "iMac":
            self.logger.info(f"{self.result}")
            assert True
            self.logger.info("********** Test Search Functionality 004 is Passed ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_search_functionality_004_failed.png")
            self.logger.error("********** Test Search Functionality 004 is Failed ***********")
            assert False
        self.logger.info("***************** End Of Test Search Functionality 004 ******************")
        self.driver.quit()

    @pytest.mark.sanity
    def test_search_functionality_005(self, setup):
        self.driver = setup
        self.logger.info("****************** Test Search Functionality 005 Is Started ***************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base URL")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("Mac")
        self.logger.info("Entering the search text 'Mac' ")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.logger.info("*************** Verifying Test Search Functionality 005 ****************")
        self.listOfProducts = self.driver.find_elements(By.XPATH, "//div[@class='product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12']/div/div[2]/div/h4/a")
        for product in self.listOfProducts:
            if len(self.listOfProducts)>1 and product.text.__contains__('Mac'):
                assert True
                self.logger.info("************ Test Search Functionality 005 is Passed *************")
            else:
                self.logger.error("************ Test Search Functionality 005 is Failed *************")
                self.driver.save_screenshot(".\\Screenshots\\test_search_functionality_005_failed.png")
        self.driver.close()
        self.logger.info("**************** End Of Test Search Functionality 005 ******************")

