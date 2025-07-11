import pytest
from selenium.webdriver.common.by import By

from pageObjects.AddToCartPage import AddToCartPage
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.ProductDisplayPage import ProductDisplayPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


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
            self.logger.error("************** Test Shopping Cart 001 is Failed **************")
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
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_add_to_cart_button_on_product_display_in_search_result()
        self.logger.info("Clicking on the add to cart button on product display in search result")
        self.sc = ShoppingCartPage(self.driver)
        self.sc.click_on_shopping_cart_header_option()
        self.logger.info("Clicking on the shopping cart header option")
        self.logger.info("*************************** Verifying Test Shopping Cart 002 ****************************")
        if self.driver.title == "Shopping Cart":
            assert True
            self.logger.info("****************** Test Shopping Cart 002 is Passed *****************")
        else:
            self.logger.error(f"Actual Title is: {self.driver.title}")
            self.logger.error("****************** Test Shopping Cart 002 is Failed *****************")
            assert False
        self.logger.info("*************************** End Of Test Shopping Cart 002 ****************************")

    @pytest.mark.sanity
    def test_shopping_cart_003(self, setup):
        self.logger.info("*************************** Test Shopping Cart 003 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_add_to_cart_button_on_product_display_in_search_result()
        self.logger.info("Clicking on the add to cart button on product display in search result")
        self.sc = ShoppingCartPage(self.driver)
        self.sc.click_on_site_map_footer_option()
        self.logger.info("Clicking on the site map footer option")
        self.sc.click_on_shopping_cart_link()
        self.logger.info("Clicking on the shopping cart link")
        self.logger.info("*************************** Verifying Test Shopping Cart 003 ****************************")
        if self.driver.title == "Shopping Cart":
            assert True
            self.logger.info(f"Actual title is: {self.driver.title}")
            self.logger.info("**************** Test Shopping Cart 003 is Passed ***************")
        else:
            self.logger.info(f"Actual title is: {self.driver.title}")
            self.logger.error("**************** Test Shopping Cart 003 is Failed ***************")
            assert False
        self.logger.info("*************************** End Of Test Shopping Cart 003 ****************************")

    @pytest.mark.sanity
    def test_shopping_cart_004(self, setup):
        self.logger.info("*************************** Test Shopping Cart 004 is Start *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_cart_button_in_black_color_beside_of_search_icon()
        self.logger.info("Clicking on the cart button")
        act_text_message = self.driver.find_element(By.XPATH, "//p[@class='text-center']")
        self.logger.info("*************************** Verifying Test Shopping Cart 004 *************************")
        if act_text_message.text == "Your shopping cart is empty!":
            act_text_message.click()
            if self.driver.title == "Your Store":
                assert True
                self.logger.info("***************** Test Shopping Cart 004 is Passed ***************")
            else:
                self.logger.error("***************** Test Shopping Cart 004 is Failed ***************")
                assert False
        else:
            self.logger.error("***************** Test Shopping Cart 004 is Failed ***************")
            assert False
        self.logger.info("*************************** End Of Test Shopping Cart 004 *************************")

    @pytest.mark.sanity
    def test_shopping_cart_005(self, setup):
        self.logger.info("**************************** Test Shopping Cart 005 is Start *****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_add_to_cart_button_on_product_display_in_search_result()
        self.logger.info("Clicking on the add to cart button")
        self.atc.click_on_cart_button_in_black_color_beside_of_search_icon()
        self.logger.info("Clicking on the cart button beside of search icon")
        self.atc.click_on_view_cart_option()
        self.logger.info("Clicking on the view cart option")
        self.logger.info("**************************** Verifying Test Shopping Cart 005 *****************************")
        if self.driver.title == "Shopping Cart":
            assert True
            self.logger.info("**************** Test Shopping Cart is Passed! ***************")
        else:
            self.logger.error("**************** Test Shopping Cart is Failed! ***************")
            assert False
        self.logger.info("**************************** End Of Test Shopping Cart 005 *****************************")

    @pytest.mark.skip("Pending details on the weight of different products from the client")
    @pytest.mark.sanity
    def test_shopping_cart_006(self, setup):
        self.logger.info("**************************** Test Shopping Cart 006 is Start ****************************")
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
        self.pd = ProductDisplayPage(self.driver)
        self.pd.click_on_add_to_cart_button_on_product_display_page()
        self.logger.info("Clicking on the add to cart button on product display page")
        self.pc.click_on_shopping_cart_link()
        self.logger.info("Clicking on the shopping cart link")
        self.logger.info("**************************** Verifying Test Shopping Cart 006 ****************************")
        if self.driver.title == "Shopping Cart":
            assert True
            self.logger.info("************** Test Shopping Cart 006 is Passed *************")
        else:
            self.logger.error("************** Test Shopping Cart 006 is Failed *************")
            assert False
        self.logger.info("**************************** End Of Test Shopping Cart 006 ****************************")



















