import pytest
from pageObjects.AddToCartPage import AddToCartPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.SearchPage import SearchPage
from pageObjects.WishListPage import WishListPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures('setup', 'log_on_failure')
class Test_009_Wish_List:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_wish_list_001(self, setup):
        self.logger.info("*************************** Test Wish List 001 is Start ***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("Clicking on the my account")
        self.lp.click_on_login_link()
        self.logger.info("Clicking on the login link")
        self.lp.set_username(self.username)
        self.logger.info("Entering username")
        self.lp.set_password(self.password)
        self.logger.info("Entering password")
        self.lp.click_on_login_button()
        self.logger.info("Clicking on the login link")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_displayed_in_product_display_page()
        self.logger.info("Clicking on the wish list option in displayed on the product display page")
        self.logger.info("*************************** Verifying Test Wish List 001 ***************************")
        if self.pc.success_message().__contains__('Success: You have added iMac to your wish list!'):
            self.wl.click_on_wish_list_link_in_success_message()
            self.logger.info("Clicking on the wish list link on the success message")
            self.atc = AddToCartPage(self.driver)
            if self.atc.is_title_of_the_page("My Wish List"):
                if self.wl.get_product_from_my_wish_list_page() == "iMac":
                    assert True
                    self.logger.info("**************** Test wish list 001 is Passed ****************")
                else:
                    self.logger.error("**************** Test wish list 001 is Failed ****************")
                    assert False
            else:
                self.logger.error("**************** Test wish list 001 is Failed ****************")
                assert False
        else:
            self.logger.error("**************** Test wish list 001 is Failed ****************")
            assert False
        self.logger.info("*************************** End Of Test Wish List 001 ***************************")
