import pytest
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.SearchPage import SearchPage
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.ProductDisplayPage import ProductDisplayPage
from pageObjects.ShoppingCartPage import ShoppingCartPage


@pytest.mark.usefixtures("setup", "log_on_failure")
class Test_010_Shopping_Cart:
    logger = LogGen.loggen()
    baseURL = ReadConfig.get_application_url()

    @pytest.mark.sanity
    def test_shopping_cart_001(self, setup):
        self.logger.info("*************************** Test Shopping Cart 001 is Start ***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("imac")
        self.logger.info("Entering the iMac to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in the search result")
        self.pd = ProductDisplayPage(self.driver)
        self.pd.click_on_add_to_cart_button_on_product_display_page()
        self.logger.info("Clicking on the add to cart button on product display page")
        self.pc.click_on_shopping_cart_link()
        self.logger.info("Clicking on the shopping cart link in success message")
        self.logger.info("*************************** Verifying Test Shopping Cart 001 ***************************")
        if self.driver.title == "Shopping Cart":
            assert True
            self.logger.info("************** Test Shopping Cart 001 is Passed **************")
        else:
            self.logger.error("************** Test Shopping Cart 001 is Passed **************")
            assert False
        self.logger.info("*************************** End Of Test Shopping Cart 001 ***************************")

    @pytest.mark.sanity
    def test_shopping_cart_002(self, setup):
        self.logger.info("*************************** Test Shopping Cart 002 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.sc = ShoppingCartPage(self.driver)
        self.sc.click_on_shopping_cart_header_option()
        self.logger.info("Clicking on the shopping cart header option")
        self.logger.info("*************************** Verifying Test Shopping Cart 002 ****************************")
        if self.driver.title == "Shopping Cart":
            assert True
            self.logger.info("****************** Test Shopping Cart 002 is Passed *****************")
        else:
            self.logger.error(f"Actual Title is: {self.driver.title}")
            self.logger.error("****************** Test Shopping Cart 002 is Passed *****************")
            assert False
        self.logger.info("*************************** End Of Test Shopping Cart 002 ****************************")







