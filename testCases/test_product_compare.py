import pytest
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductComparePage import ProductComparePage
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
