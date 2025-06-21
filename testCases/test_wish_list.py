import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageObjects.AddToCartPage import AddToCartPage
from pageObjects.LoginPage import LoginPage
from pageObjects.LogoutPage import LogoutPage
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
        if 'Success: You have added iMac to your wish list!' in self.pc.success_message():
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
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
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

    @pytest.mark.sanity
    def test_wish_list_007(self, setup):
        self.logger.info("*************************** Test Wish List 007 is Start ***************************")
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
        self.logger.info("Entering the iMac product name to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_displayed_in_product_display_page()
        self.logger.info("Clicking on the add to wish list option in product display page")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_wish_list_header_option()
        self.logger.info("Clicking on the wish list header option")
        self.logger.info("*************************** Verifying Test Wish List 007 ***************************")
        if self.atc.is_title_of_the_page("My Wish List"):
            assert True
            self.logger.info("***************** Test Wish List 007 is Passed ****************")
        else:
            self.logger.error("***************** Test Wish List 007 is Failed ****************")
            assert False
        self.logger.info("*************************** End Of Test Wish List 007 ***************************")

    @pytest.mark.sanity
    def test_wish_list_008(self, setup):
        self.logger.info("******************************* Test Wish List 008 is Start ********************************")
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
        self.wl = WishListPage(self.driver)
        self.wl.click_on_wish_list_option_from_right_column()
        self.logger.info("Clicking on the wish list option from right column")
        self.logger.info(
            "******************************* Verifying Test Wish List 008 ********************************")
        self.atc = AddToCartPage(self.driver)
        if self.atc.is_title_of_the_page("My Wish List"):
            assert True
            self.logger.info("**************** Test Wish List 008 is Passed ****************")
        else:
            self.logger.error("**************** Test Wish List 008 is Failed ****************")
            assert False
        self.logger.info("******************************* End Of Test Wish List 008 ********************************")

    @pytest.mark.sanity
    def test_wish_list_009(self, setup):
        self.logger.info("******************************* Test Wish List 009 is Start ********************************")
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
        self.wl = WishListPage(self.driver)
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the modify your wish list option")
        self.logger.info(
            "******************************* Verifying Test Wish List 009 ********************************")
        self.atc = AddToCartPage(self.driver)
        if self.atc.is_title_of_the_page("My Wish List"):
            assert True
            self.logger.info("**************** Test Wish List 009 is Passed ****************")
        else:
            self.logger.error("**************** Test Wish List 009 is Failed ****************")
            assert False
        self.logger.info("******************************* End Of Test Wish List 009 ********************************")

    @pytest.mark.sanity
    def test_wish_list_010(self, setup):
        self.logger.info("******************************* Test Wish List 010 is Start ********************************")
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
        self.wl = WishListPage(self.driver)
        self.wl.click_on_wish_list_link_from_footer_option()
        self.logger.info("Clicking on the  wish list link from footer option")
        self.logger.info(
            "******************************* Verifying Test Wish List 010 ********************************")
        self.atc = AddToCartPage(self.driver)
        if self.atc.is_title_of_the_page("My Wish List"):
            assert True
            self.logger.info("**************** Test Wish List 010 is Passed ****************")
        else:
            self.logger.error("**************** Test Wish List 010 is Failed ****************")
            assert False
        self.logger.info("******************************* End Of Test Wish List 010 ********************************")

    @pytest.mark.sanity
    def test_wish_list_011(self, setup):
        self.logger.info("******************************* Test Wish List 011 is Start ********************************")
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
        self.wl = WishListPage(self.driver)
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the  wish list link from footer option")
        self.logger.info("****************************** Verifying Test Wish List 011 *******************************")
        account_breadcrumb = self.driver.find_element(By.LINK_TEXT, "Account")
        my_wish_list_breadcrumb = self.driver.find_element(By.LINK_TEXT, "My Wish List")
        if account_breadcrumb.is_displayed() and my_wish_list_breadcrumb.is_displayed():
            self.atc = AddToCartPage(self.driver)
            if self.atc.is_title_of_the_page("My Wish List"):
                account_breadcrumb.click()
                if self.atc.is_title_of_the_page("My Account"):
                    assert True
                    self.logger.info("**************** Test Wish List 011 is Passed ***************")
                else:
                    self.logger.error("**************** Test Wish List 011 is Failed ***************")
            else:
                self.logger.error("**************** Test Wish List 011 is Failed ***************")
        else:
            self.logger.error("**************** Test Wish List 011 is Failed ***************")
        self.logger.info("****************************** End Of Test Wish List 011 *******************************")

    @pytest.mark.sanity
    def test_wish_list_012(self, setup):
        self.logger.info("******************************* Test Wish List 012 is Start ********************************")
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
        self.wl = WishListPage(self.driver)
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the  wish list link from footer option")
        self.logger.info("****************************** Verifying Test Wish List 012 *******************************")
        self.atc = AddToCartPage(self.driver)
        if self.atc.is_title_of_the_page("My Wish List"):
            if self.driver.current_url == "https://tutorialsninja.com/demo/index.php?route=account/wishlist":
                heading = self.driver.find_element(By.XPATH, "//h2[normalize-space()='My Wish List']").text
                if heading == "My Wish List":
                    assert True
                    self.logger.info("***************** Test Wish List 012 is Passed *****************")
                else:
                    self.logger.error("***************** Test Wish List 012 is Failed *****************")
                    assert False
            else:
                self.logger.error("***************** Test Wish List 012 is Failed *****************")
                assert False
        else:
            self.logger.error("***************** Test Wish List 012 is Failed *****************")
            assert False
        self.logger.info("****************************** End Of Test Wish List 012 *******************************")

    @pytest.mark.sanity
    def test_wish_list_013(self, setup):
        self.logger.info("******************************* Test Wish List 013 is Start ********************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("Login successful")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the modify your wish list option")
        if self.wl.clear_wishlist_if_not_empty():
            self.logger.info("Wish list is empty or cleared successfully")
            self.lO = LogoutPage(self.driver)
            self.lO.click_on_continue_button()
            self.logger.info("Clicking on continue button")
            self.atc = AddToCartPage(self.driver)
            if self.atc.is_title_of_the_page("My Account"):
                self.logger.info("**************** Test Wish List 013 is Passed ***************")
                assert True
            else:
                self.logger.error("Page title validation failed")
                self.logger.error("**************** Test Wish List 013 is Failed ***************")
                assert False
        else:
            self.logger.error("Failed to clear wish list or detect its state")
            self.logger.error("**************** Test Wish List 013 is Failed ***************")
            assert False
        self.logger.info("****************************** End Of Test Wish List 013 *******************************")

    @pytest.mark.sanity
    def test_wish_list_014(self, setup):
        self.logger.info("**************************** Test Wish List 014 is Start *****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("Login successful")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_wish_list_header_option()
        self.logger.info("Clicking on the wish list header option")
        self.wl = WishListPage(self.driver)
        self.wl.clear_wishlist_if_not_empty()
        self.logger.info("Clearing wish list if not empty")
        self.lo = LogoutPage(self.driver)
        self.lo.click_on_continue_button()
        self.logger.info("Clicking on the continue button")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product name to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the add to wish list option display in search result")
        self.wl.click_on_search_breadcrumb_option()
        self.logger.info("Clicking on the search breadcrumb option")
        self.driver.back()
        self.logger.info("Clicking on the back arrow on the browser")
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the modify your wish list option")
        self.logger.info("**************************** Verifying Test Wish List 014 *****************************")
        l = []
        exp_list = ['iMac', 'Product 14', 'Out Of Stock', '$122.00']
        data = self.driver.find_elements(By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr/td")
        for item in data:
            # if data[0] == item:
            #     item.is_displayed()
            #     self.logger.info("Image is display")
            #
            # if data[5] == item:
            #     item.is_displayed()
            #     self.logger.info("Action buttons is display")

            l.append(item.text)
        cleaned_data_list = [item for item in l if item.strip()]
        image = self.driver.find_element(By.XPATH, "(//img[@title='iMac'])[2]")
        action_buttons = self.driver.find_element(By.XPATH, "(//td)[25]")
        if image.is_displayed():
            self.logger.info("Product image is display")
            if action_buttons.is_displayed():
                self.logger.info("Action buttons is display")
                if cleaned_data_list == exp_list:
                    self.logger.info("Proper details are display")
                    image.click()
                    self.logger.info("Clicking on the image")
                    self.atc = AddToCartPage(self.driver)
                    if self.atc.is_title_of_the_page("iMac"):
                        self.driver.back()
                        self.lo = LogoutPage(self.driver)
                        self.lo.click_on_continue_button()
                        self.logger.info("Clicking on the continue button")
                        if self.atc.is_title_of_the_page("My Account"):
                            assert True
                            self.logger.info("*************** Test Wish List 014 is Passed **************")
                        else:
                            self.logger.info(f"My Account page title is Failed: (Actual title is {self.driver.title})")
                            self.logger.error("*************** Test Wish List 014 is Failed **************")
                            assert False
                    else:
                        self.logger.info(f"iMac page title is Failed: (Actual title is {self.driver.title})")
                        self.logger.error("*************** Test Wish List 014 is Failed **************")
                        assert False
                else:
                    self.logger.info("Proper details is not display")
                    self.logger.error("*************** Test Wish List 014 is Failed **************")
                    assert False
            else:
                self.logger.info("Action buttons is not display")
                self.logger.error("*************** Test Wish List 014 is Failed **************")
                assert False
        else:
            self.logger.info("Image is not display")
            self.logger.error("*************** Test Wish List 014 is Failed **************")
            assert False
        self.logger.info("**************************** End Of Test Wish List 014 *****************************")

    @pytest.mark.sanity
    def test_wish_list_015(self, setup):
        self.logger.info("**************************** Test Wish List 015 is Start *****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product name to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the add to wish list option")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("Login successful")
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the modify your wish list option")
        self.wl.clear_wishlist_if_not_empty()
        self.logger.info("Clearing wish list if not empty")
        self.logger.info("**************************** Verifying Test Wish List 015 *****************************")
        text_message = self.driver.find_element(By.XPATH, "//p[normalize-space()='Your wish list is empty.']").text
        self.pc = ProductComparePage(self.driver)
        if self.pc.success_message().__contains__('Success: You have modified your wish list!'):
            if text_message == 'Your wish list is empty.':
                assert True
                self.logger.info("************** Test Wish List 015 is Passed ************")
            else:
                self.logger.error("************** Test Wish List 015 is Failed ************")
                assert False
        else:
            self.logger.error("************** Test Wish List 015 is Failed ************")
            assert False
        self.logger.info("**************************** End Of Test Wish List 015 *****************************")

    @pytest.mark.sanity
    def test_wish_list_016(self, setup):
        self.logger.info("*************************** Test Wish List 016 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.sf.click_on_search_button()
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("adding product to my wish list")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("Login is successful")
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the modify your wish list option")
        self.pc = ProductComparePage(self.driver)
        self.wl.click_on_add_to_cart_button_in_wish_list()
        self.logger.info("Clicking on the add to cart button")
        self.logger.info("*************************** Verifying Test Wish List 016 ****************************")
        if 'Success: You have added iMac to your shopping cart!' in self.pc.success_message():
            assert True
            self.logger.info("*************** Test Wish List 016 is Passed ***************")
        else:
            self.logger.error("*************** Test Wish List 016 is Failed ***************")
        self.logger.info("*************************** End Of Test Wish List 016 ****************************")

    @pytest.mark.sanity
    def test_wish_list_017(self, setup):
        self.logger.info("*************************** Test Wish List 017 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")

        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("Login is successful")

        self.wl = WishListPage(self.driver)
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the modify your wish list option")
        self.wl.clear_wishlist_if_not_empty()
        self.logger.info("Clearing all my wish list")

        self.driver.back()
        self.wl.click_on_account_breadcrumb_option()
        self.logger.info("Clicking on the account breadcrumb option")

        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.sf.click_on_search_button()
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.sf.search_product("iphone")
        self.sf.click_on_search_button()
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.sf.search_product("MacBook Air")
        self.sf.click_on_search_button()
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.sf.search_product("MacBook")
        self.sf.click_on_search_button()
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("adding multiple product to my wish list")
        self.wl.click_on_wish_list_link_in_success_message()
        self.logger.info("Clicking on wish list link in success message")
        self.logger.info("*************************** Verifying Test Wish List 017 ****************************")
        self.atc = AddToCartPage(self.driver)
        l = []
        exp_list = ['iPhone', 'product 11', 'Out Of Stock', '$123.20', 'iMac', 'Product 14', 'Out Of Stock', '$122.00',
                    'MacBook', 'Product 16', 'Out Of Stock', '$602.00', 'MacBook Air', 'Product 17', 'Out Of Stock',
                    '$1,202.00']
        if self.atc.is_title_of_the_page("My Wish List"):
            all_images = self.driver.find_elements(By.XPATH,
                                                   "//table[@class='table table-bordered table-hover']/tbody/tr/td[1]")
            for image in all_images:
                image.is_displayed()
            self.logger.info("All the images of the product are display and its works as expected")
            all_product_name = self.driver.find_elements(By.XPATH,
                                                         "//table[@class='table table-bordered table-hover']/tbody/tr/td[2]")
            for product_name in all_product_name:
                product_name.is_displayed()
            self.logger.info("All the product name are display, and it works as expected")

            data = self.driver.find_elements(By.XPATH, "//table[@class='table table-bordered table-hover']/tbody/tr/td")
            for item in data:
                l.append(item.text)
            cleaned_data_list = [item for item in l if item.strip()]
            if exp_list == cleaned_data_list:
                assert True
                self.logger.info("************** Test Wish List 017 is Passed **************")
            else:
                self.logger.info(f"{cleaned_data_list}")
                self.logger.error("************** Test Wish List 017 is Failed **************")
                assert False
        else:
            self.logger.info(f"title is failed: Actual title is -> {self.driver.title}")
            self.logger.error("************** Test Wish List 017 is Failed **************")
            assert False
        self.logger.info("*************************** End Of Test Wish List 017 ****************************")

    @pytest.mark.sanity
    def test_wish_list_018(self, setup):
        self.logger.info("************************** Test Wish List 018 is Start ****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.lp = LoginPage(self.driver)
        self.lp.click_on_my_account()
        self.lp.click_on_login_link()
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_on_login_button()
        self.logger.info("Login is Successful")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_modify_your_wish_list_option()
        self.logger.info("Clicking on the modify your wish list option")
        self.wl.clear_wishlist_if_not_empty()
        self.logger.info("Clearing all my wish list")
        self.driver.back()
        self.wl.click_on_account_breadcrumb_option()
        self.logger.info("Clicking on the account breadcrumb option")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.wl = WishListPage(self.driver)
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the add to wish list option")
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the add to wish list option")
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the add to wish list option")
        self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the add to wish list option")
        self.wl.click_on_wish_list_link_in_success_message()
        self.logger.info("Clicking on the wish list link in success message")
        self.logger.info("************************** Verifying Test Wish List 018 ****************************")
        self.atc = AddToCartPage(self.driver)
        if self.atc.is_title_of_the_page("My Wish List"):
            self.logger.info("Page title is passed")
            if self.wl.is_product_name_from_my_wish_list_page("iMac"):
                self.logger.info("Product name is passed")
                products = self.driver.find_elements(*self.wl.productName)
                if len(products) == 1:
                    assert True
                    self.logger.info("Length of product is: 1")
                    self.logger.info("*************** Test Wish List 018 is Passed ***************")
                else:
                    self.logger.error("*************** Test Wish List 018 is Failed ***************")
                    assert False
            else:
                self.logger.error("*************** Test Wish List 018 is Failed ***************")
                assert False
        else:
            self.logger.error("*************** Test Wish List 018 is Failed ***************")
            assert False
        self.logger.info("************************** End Of Test Wish List 018 ****************************")

    @pytest.mark.sanity
    def test_wish_list_019(self, setup):
        self.logger.info("***************************** Test Wish List 019 is Start *******************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.wl = WishListPage(self.driver)
        self.atc = AddToCartPage(self.driver)
        wish_list_header_option = self.wl.is_enable_and_is_display(self.atc.wishListHeaderOption)
        self.logger.info("***************************** Verifying Test Wish List 019 *******************************")
        if wish_list_header_option:
            add_to_wish_list_option_feature = self.wl.is_enable_and_is_display(self.wl.wishListOptionFromFeaturePage)
            if add_to_wish_list_option_feature:
                wish_list_link_footer = self.wl.is_enable_and_is_display(self.wl.wishListLinkFromFooterOption)
                if wish_list_link_footer:
                    self.lp = LoginPage(self.driver)
                    self.lp.click_on_my_account()
                    self.lp.click_on_login_link()
                    self.lp.set_username(self.username)
                    self.lp.set_password(self.password)
                    self.lp.click_on_login_button()
                    self.logger.info("Login is Successful")
                    modify_your_wish_list_option = self.wl.is_enable_and_is_display(self.wl.modifyYourWishListOption)
                    if modify_your_wish_list_option:
                        wish_list_option_from_right_column = self.wl.is_enable_and_is_display(
                            self.wl.wishListOptionFromRightColumn)
                        if wish_list_option_from_right_column:
                            self.wl.click_on_modify_your_wish_list_option()
                            self.logger.info("Clicking on modify your wish list option")
                            my_wish_list_breadcrumb_option = self.wl.is_enable_and_is_display(
                                self.wl.myWishListBreadcrumbOption)
                            if my_wish_list_breadcrumb_option:
                                self.sf = SearchPage(self.driver)
                                self.sf.search_product("iMac")
                                self.logger.info("Entering iMac to search text box field")
                                self.sf.click_on_search_button()
                                self.logger.info("Clicking on the search icon button")
                                add_to_wish_list_option_product_display_search_result = self.wl.is_enable_and_is_display(
                                    self.wl.addToWishListOptionInSearchResultPage)
                                if add_to_wish_list_option_product_display_search_result:
                                    self.wl.click_on_add_to_wish_list_option_on_the_product_display_in_search_result()
                                    self.logger.info("Clicking on the add to wish list option search result")
                                    wish_list_link_in_success_message = self.wl.is_enable_and_is_display(
                                        self.wl.wishListLink)
                                    if wish_list_link_in_success_message:
                                        assert True
                                        self.logger.info("*************** Test Wish List 019 is Passed ***************")
                                    else:
                                        self.logger.error("*************** Test Wish List 019 is Failed ***************")
                                        assert False
                                else:
                                    self.logger.error("*************** Test Wish List 019 is Failed ***************")
                                    assert False
                            else:
                                self.logger.error("*************** Test Wish List 019 is Failed ***************")
                                assert False
                        else:
                            self.logger.error("*************** Test Wish List 019 is Failed ***************")
                            assert False
                    else:
                        self.logger.error("*************** Test Wish List 019 is Failed ***************")
                        assert False
                else:
                    self.logger.error("*************** Test Wish List 019 is Failed ***************")
                    assert False
            else:
                self.logger.error("*************** Test Wish List 019 is Failed ***************")
                assert False
        else:
            self.logger.error("*************** Test Wish List 019 is Failed ***************")
            assert False
        self.logger.info("***************************** End Of Test Wish List 019 *******************************")






