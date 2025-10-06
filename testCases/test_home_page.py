import pytest
from selenium.webdriver import ActionChains

from utilities.customLogger import LogGen
from pageObjects.SearchPage import SearchPage
from utilities.readProperties import ReadConfig
from pageObjects.AddToCartPage import AddToCartPage
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.WishListPage import WishListPage
from pageObjects.HomePage import HomePage
from pageObjects.LogoutPage import LogoutPage

@pytest.mark.usefixtures("setup", "log_on_failure")
class Test_011_Home_Page:
    logger = LogGen.loggen()
    baseURL = ReadConfig.get_application_url()

    @pytest.mark.sanity
    def test_home_page_001(self, setup):
        self.logger.info("************************* Test Home Page 001 is Start *************************")
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
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_shopping_cart_link()
        self.logger.info("Clicking on the shopping cart link in success message")
        self.hp = HomePage(self.driver)
        self.hp.click_on_continue_shopping_button()
        self.logger.info("Clicking on the continue shopping button")
        self.logger.info("************************* Verifying Test Home Page 001 *************************")
        if self.driver.title == "Your Store":
            assert True
            self.logger.info("************* Test Home Page 001 is Passed *************")
        else:
            self.logger.error(f"Actual title: {self.driver.title}  Expected title: Your Store")
            self.logger.error("************* Test Home Page 001 is Failed *************")
            assert False
        self.logger.info("************************* End Of Test Home Page 001 *************************")

    @pytest.mark.skip("order success page is not available yet")
    @pytest.mark.sanity
    def test_home_page_002(self, setup):
        pass

    @pytest.mark.sanity
    def test_home_page_003(self, setup):
        self.logger.info("************************* Test Home Page 003 is Start *************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_wish_list_link_from_footer_option()
        self.logger.info("Clicking on the wish list footer option")
        self.wl.click_on_store_logo()
        self.logger.info("Clicking on the store logo")
        self.logger.info("************************* Verifying Test Home Page 003 *************************")
        if self.driver.title == "Your Store":
            assert True
            self.logger.info("**************** Test Home Page 003 is Passed ***************")
        else:
            self.logger.error("**************** Test Home Page 003 is Failed ***************")
            assert False
        self.logger.info("************************* End Of Test Home Page 003 *************************")

    @pytest.mark.sanity
    def test_home_page_004(self, setup):
        self.logger.info("*************************** Test Home Page 004 is Start *******************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.desktops_option()).perform()
        self.logger.info("hovering on desktop option")
        self.hp = HomePage(self.driver)
        self.hp.pc_zero_product_option()
        self.logger.info("Clicking on zero product option")
        self.lo = LogoutPage(self.driver)
        self.lo.click_on_continue_button()
        self.logger.info("Clicking on continue button")
        self.logger.info("************************* Verifying Test Home Page 004 ***************************")
        if self.driver.title == "Your Store":
            assert True
            self.logger.info("************ Test Home Page 004 Passed ************")
        else:
            self.logger.error("************ Test Home Page 004 Failed ************")
            assert False
        self.logger.info("************************* End of Test Home Page 004 ***************************")







