import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.SearchPage import SearchPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures('setup', 'log_on_failure')
class Test_006_Product_Compare:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_product_compare_001(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 001 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.sp = SearchPage(self.driver)
        self.sp.search_product("iMac")
        self.logger.info("Entering iMac product for search")
        self.sp.click_on_search_button()
        self.logger.info("clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_imac_product()
        self.logger.info("Clicking on the Product displayed in the Search results")
        self.logger.info("*************** Verifying Test Product Compare 001 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                      "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/button[2]")
        if self.tooltip_text.get_attribute("data-original-title")== "Compare this Product":
            self.pc.click_on_compare_this_product_option()
            self.logger.info("clicking on compare this product option")
            if self.pc.success_message().__contains__("Success: You have added iMac to your product comparison!"):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 001 is Passed ***********")
                else:
                    self.logger.error("********** Test Product Compare 001 is Failed ***********")
                    assert False
            else:
                self.logger.error("********** Test Product Compare 001 is Failed ***********")
                assert False
        else:
            self.logger.error("********** Test Product Compare 001 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 001 *************************")

    @pytest.mark.sanity
    def test_product_compare_002(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 002 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.sp = SearchPage(self.driver)
        self.sp.search_product("iMac")
        self.logger.info("Entering iMac product for search")
        self.sp.click_on_search_button()
        self.logger.info("clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_list_view_button()
        self.logger.info("Clicking on list view button")
        self.logger.info("*************** Verifying Test Product Compare 002 ****************")

        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//button[3][contains(@data-original-title,'Compare this Product')]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.compare_this_product_option_available_on_the_product()
            self.logger.info("clicking on compare this product option available on the Product that is displayed in the Search")
            if self.pc.success_message().__contains__("Success: You have added iMac to your product comparison!"):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 002 is Passed ***********")
                else:
                    self.logger.error("********** Test Product Compare 002 is Failed ***********")
                    assert False
            else:
                self.logger.error("********** Test Product Compare 002 is Failed ***********")
                assert False
        else:
            print(self.tooltip_text.get_attribute("data-original-title"))
            self.logger.error("********** Test Product Compare 002 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 002 *************************")

    @pytest.mark.sanity
    def test_product_compare_003(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 003 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.sp = SearchPage(self.driver)
        self.sp.search_product("iMac")
        self.logger.info("Entering iMac product for search")
        self.sp.click_on_search_button()
        self.logger.info("clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_grid_view_button()
        self.logger.info("Clicking on grid view button")
        self.logger.info("*************** Verifying Test Product Compare 003 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//button[3][contains(@data-original-title,'Compare this Product')]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.compare_this_product_option_available_on_the_product()
            self.logger.info("clicking on compare this product option available on the Product that is displayed in the Search")
            if self.pc.success_message().__contains__("Success: You have added iMac to your product comparison!"):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                time.sleep(1)
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 003 is Passed ***********")
                else:
                    self.logger.error("********** Test Product Compare 003 is Failed ***********")
                    assert False
            else:
                self.logger.error("********** Test Product Compare 003 is Failed ***********")
                assert False
        else:
            print(self.tooltip_text.get_attribute("data-original-title"))
            self.logger.error("********** Test Product Compare 003 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 003 *************************")

    @pytest.mark.sanity
    def test_product_compare_004(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 004 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("hovering on desktops option and clicking on show all desktops option")
        self.pc.click_on_list_view_button()
        self.logger.info("Clicking on list view button")
        self.logger.info("*************** Verifying Test Product Compare 004 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//*[@id='content']/div[4]/div[1]/div/div[2]/div[2]/button[3]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.compare_this_product_option_available_on_the_product()
            self.logger.info(
                "clicking on compare this product option available on the Product that is displayed in the Product Category page")
            if self.pc.success_message().__contains__('Success: You have added Apple Cinema 30" to your product comparison!'):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 004 is Passed ***********")
                else:
                    self.logger.info(f"{self.driver.title}")
                    self.logger.error("********** Test Product Compare 004 is Failed ***********")
                    assert False
            else:
                self.logger.info(f"{self.pc.success_message()}")
                self.logger.error("********** Test Product Compare 004 is Failed ***********")
                assert False
        else:
            self.logger.info(f"{self.tooltip_text.get_attribute("data-original-title")}")
            self.logger.error("********** Test Product Compare 004 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 004 *************************")

    @pytest.mark.sanity
    def test_product_compare_005(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 005 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(
            self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("hovering on desktops option and clicking on show all desktops option")
        self.pc.click_on_grid_view_button()
        self.logger.info("Clicking on grid view button")
        self.logger.info("*************** Verifying Test Product Compare 005 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//*[@id='content']/div[4]/div[1]/div/div[2]/div[2]/button[3]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.compare_this_product_option_available_on_the_product()
            self.logger.info(
                "clicking on compare this product option available on the Product that is displayed in the Product Category page")
            if self.pc.success_message().__contains__(
                    'Success: You have added Apple Cinema 30" to your product comparison!'):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 005 is Passed ***********")
                else:
                    self.logger.info(f"{self.driver.title}")
                    self.logger.error("********** Test Product Compare 005 is Failed ***********")
                    assert False
            else:
                self.logger.info(f"{self.pc.success_message()}")
                self.logger.error("********** Test Product Compare 005 is Failed ***********")
                assert False
        else:
            self.logger.info(f"{self.tooltip_text.get_attribute("data-original-title")}")
            self.logger.error("********** Test Product Compare 005 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 005 *************************")



