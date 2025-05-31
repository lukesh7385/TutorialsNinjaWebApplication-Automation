import pytest
from selenium.webdriver.common.by import By
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.ProductDisplayPage import ProductDisplayPage

@pytest.mark.usefixtures("setup", "log_on_failure")
class Test_008_Add_To_Cart:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    def test_add_to_cart_001(self, setup):
        self.driver = setup
        self.logger.info("***************************** Test Add To Cart 001 is Start *****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.pd = ProductDisplayPage(self.driver)
        self.pd.click_on_add_to_cart_button_on_product_display_page()
        self.logger.info("Clicking on the add to cart button")
        self.logger.info("***************************** Verifying Test Add To Cart 001 *****************************")
        if self.pc.success_message().__contains__('Success: You have added iMac to your shopping cart!'):
            self.pc.click_on_shopping_cart_link()
            if self.driver.title == "Shopping Cart":
                product_name = self.driver.find_element(By.LINK_TEXT, "iMac").text
                if product_name == "iMac":
                    assert True
                    self.logger.info("************** Test Add To Cart 001 is Passed **************")
                else:
                    self.logger.error("************** Test Add To Cart 001 is Failed **************")
                    assert False
            else:
                self.logger.error("************** Test Add To Cart 001 is Failed **************")
                assert False
        else:
            self.logger.error("************** Test Add To Cart 001 is Failed **************")
            assert False
        self.logger.info("***************************** End Of Test Add To Cart 001 *****************************")

