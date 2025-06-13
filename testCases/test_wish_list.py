import time
import pytest
from selenium.webdriver import ActionChains
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
        self.logger.info("Clicking on the login button")
        time.sleep(0.2)
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search text box field")
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
                if self.wl.is_product_name_from_my_wish_list_page("iMac"):
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

    @pytest.mark.sanity
    def test_wish_list_002(self, setup):
        self.logger.info("****************************** Test Wish List 002 is Start ******************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("Clicking on my account")
        self.lp.click_on_login_link()
        self.logger.info("Clicking on login link")
        self.lp.set_username(self.username)
        self.logger.info("Entering username")
        self.lp.set_password(self.password)
        self.logger.info("Entering password")
        self.lp.click_on_login_button()
        self.logger.info("Clicking on the login button")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in the search result")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_displayed_in_product_display_page()
        self.logger.info("Clicking on the wish list option")
        self.logger.info("****************************** Verifying Test Wish List 002 ******************************")
        if 'Success: You have added iMac to your wish list!' in self.pc.success_message():
            self.wl.click_on_wish_list_link_in_success_message()
            self.logger.info("Clicking on the wish list link in success message")
            if self.wl.is_product_name_from_my_wish_list_page("iMac"):
                assert True
                self.logger.info("*************** Test Wish List 002 is Passed ***************")
            else:
                self.logger.error("*************** Test Wish List 002 is Failed ***************")
                assert False
        else:
            self.logger.error("*************** Test Wish List 002 is Failed ***************")
            assert False
        self.logger.info("****************************** End Of Test Wish List 002 ******************************")

    @pytest.mark.sanity
    def test_wish_list_003(self, setup):
        self.logger.info("***************************** Test Wish List 003 is Start *********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("Clicking on my account")
        self.lp.click_on_login_link()
        self.logger.info("Clicking on login link")
        self.lp.set_username(self.username)
        self.logger.info("Entering username")
        self.lp.set_password(self.password)
        self.logger.info("Entering password")
        self.lp.click_on_login_button()
        self.logger.info("Clicking on the login button")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_store_logo()
        self.logger.info("Clicking on the store logo")
        self.atc = AddToCartPage(self.driver)
        self.logger.info("***************************** Verifying Test Wish List 003 *********************************")
        if self.atc.is_title_of_the_page("Your Store"):
            self.logger.info("page title is passed")
            self.wl.click_on_add_to_wish_list_option_on_feature_page()
            self.logger.info("Clicking on the add to wish list option on product display in feature page")
            self.pc = ProductComparePage(self.driver)
            if 'Success: You have added MacBook to your wish list!' in self.pc.success_message():
                self.logger.info("success message is passed")
                self.wl.click_on_wish_list_link_in_success_message()
                self.logger.info("Clicking on the wish list link in success message")
                if self.wl.is_product_name_from_my_wish_list_page("MacBook"):
                    self.logger.info("Expected product is display")
                    assert True
                    self.logger.info("****************** Test Wish List 003 is Passed ****************")
                else:
                    self.logger.error("****************** Test Wish List 003 is Failed ****************")
                    assert False
            else:
                self.logger.error("****************** Test Wish List 003 is Failed ****************")
                assert False
        else:
            self.logger.error("****************** Test Wish List 003 is Failed ****************")
            assert False
        self.logger.info("***************************** End Of Test Wish List 003 *********************************")

    @pytest.mark.sanity
    def test_wish_list_004(self, setup):
        self.logger.info("*************************** Test Wish List 004 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("Clicking on the my account link")
        self.lp.click_on_login_link()
        self.logger.info("Clicking on the login link")
        self.lp.set_username(self.username)
        self.logger.info("Entering username")
        self.lp.set_password(self.password)
        self.logger.info("Entering password")
        self.lp.click_on_login_button()
        self.logger.info("Clicking on the login button")
        self.pc = ProductComparePage(self.driver)
        time.sleep(1)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.desktops_option()
        ).move_to_element(self.pc.show_all_desktops_option()).click().perform()
        self.wl = WishListPage(self.driver)
        self.wl.click_on_mac_subcategory_option()
        self.logger.info("Clicking on the mac subcategory option")
        self.wl.click_on_add_to_wish_list_option_from_mac_subcategory_option()
        self.logger.info("Clicking on the add to wish list option available in mac subcategory option")
        self.logger.info("*************************** Verifying Test Wish List 004 ****************************")
        if  'Success: You have added iMac to your wish list!' in self.pc.success_message():
            self.wl.click_on_wish_list_link_in_success_message()
            self.logger.info("Clicking on the wish list link in success message")
            if self.wl.is_product_name_from_my_wish_list_page("iMac"):
                assert True
                self.logger.info("*************** Test Wish List 004 is Passed **************")
            else:
                self.logger.error("*************** Test Wish List 004 is Failed **************")
                assert False
        else:
            self.logger.error("*************** Test Wish List 004 is Failed **************")
            assert False
        self.logger.info("*************************** End Of Test Wish List 004 ****************************")

    @pytest.mark.sanity
    def test_wish_list_005(self, setup):
        self.logger.info("*************************** Test Wish List 005 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("Clicking on the my account link")
        self.lp.click_on_login_link()
        self.logger.info("Clicking on the login link")
        self.lp.set_username(self.username)
        self.logger.info("Entering username")
        self.lp.set_password(self.password)
        self.logger.info("Entering password")
        self.lp.click_on_login_button()
        self.logger.info("Clicking on the login button")
        self.sf = SearchPage(self.driver)
        time.sleep(0.2)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product name to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_display_in_search_result()
        self.logger.info("Clicking on the add wish list option display in search result page")
        self.logger.info("*************************** Verifying Test Wish List 005 ****************************")
        self.pc = ProductComparePage(self.driver)
        if 'Success: You have added iMac to your wish list!' in self.pc.success_message():
            self.wl.click_on_wish_list_link_in_success_message()
            self.logger.info("Clicking on the wish list link in success message")
            if self.wl.is_product_name_from_my_wish_list_page("iMac"):
                assert True
                self.logger.info("***************** Test Wish List 005 is Passed ****************")
            else:
                self.logger.error("***************** Test Wish List 005 is Failed ****************")
                assert False
        else:
            self.logger.error("***************** Test Wish List 005 is Failed ****************")
            assert False
        self.logger.info("*************************** End Of Test Wish List 005 ****************************")

    @pytest.mark.sanity
    def test_wish_list_006(self, setup):
        self.logger.info("************************* Test Wish List 006 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.logger.info("Clicking on the my account link")
        self.lp.click_on_login_link()
        self.logger.info("Clicking on the login link")
        self.lp.set_username(self.username)
        self.logger.info("Entering username")
        self.lp.set_password(self.password)
        self.logger.info("Entering password")
        self.lp.click_on_login_button()
        self.logger.info("Clicking on the login button")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product name to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_displayed_in_product_display_page()
        self.logger.info("Clicking on the add to wish list option in product display page")
        self.wl.click_on_wish_list_link_in_success_message()
        self.logger.info("Clicking on the wish list link in success message")
        self.logger.info("************************* Verifying Test Wish List 006 ****************************")
        self.atc = AddToCartPage(self.driver)
        if self.atc.is_title_of_the_page("My Wish List"):
            assert True
            self.logger.info("*************** Test Wish List 006 is Passed ***************")
        else:
            self.logger.error("*************** Test Wish List 006 is Failed ***************")
            assert False
        self.logger.info("************************* End Of Test Wish List 006 ****************************")














