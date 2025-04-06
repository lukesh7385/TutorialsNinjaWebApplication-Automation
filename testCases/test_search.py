import time

import allure
import pytest
from selenium.webdriver.common.by import By
from pageObjects.SearchPage import SearchPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


@pytest.mark.usefixtures('setup', 'log_on_failure')
@allure.severity(allure.severity_level.CRITICAL)
class Test_005_Search_Functionality:
    baseURL = ReadConfig.get_application_url()
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