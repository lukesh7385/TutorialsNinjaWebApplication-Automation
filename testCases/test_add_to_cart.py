import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.AddToCartPage import AddToCartPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.ProductDisplayPage import ProductDisplayPage
from pageObjects.SearchPage import SearchPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup", "log_on_failure")
class Test_008_Add_To_Cart:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
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
                if self.atc.get_product_name() == "iMac":
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

    @pytest.mark.sanity
    def test_add_to_cart_002(self, setup):
        self.driver = setup
        self.logger.info("**************************** Test Add To Cart 002 is Start ****************************")
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
        self.logger.info("Clicking on login button")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering  iMac product to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_add_to_wish_list_from_search_result()
        self.logger.info("adding product to wish list from search result")
        self.atc.click_on_wish_list_header_option()
        self.logger.info("Clicking on wish list header option")
        self.atc.click_on_add_to_cart_icon_option_from_my_wish_list()
        self.logger.info("Clicking on the add to cart option from my wish list")
        self.logger.info("**************************** Verifying Test Add To Cart 002 ****************************")
        self.pc = ProductComparePage(self.driver)
        if self.pc.success_message().__contains__('Success: You have added iMac to your shopping cart!'):
            self.atc.click_on_sopping_cart_header_option()
            self.logger.info("Clicking on sopping cart header option")
            if self.driver.title == "Shopping Cart":
                if self.atc.get_product_name() == "iMac":
                    assert True
                    self.logger.info("************* Test Add To Cart 002 is Passed ************")
                else:
                    self.logger.error("************* Test Add To Cart 002 is Failed ************")
                    assert False
            else:
                self.logger.error("************* Test Add To Cart 002 is Failed ************")
                assert False
        else:
            self.logger.error("************* Test Add To Cart 002 is Failed ************")
            assert False
        self.logger.info("**************************** End Of Test Add To Cart 002 ****************************")

    @pytest.mark.sanity
    def test_add_to_cart_003(self, setup):
        self.driver = setup
        self.logger.info("**************************** Test Add To Cart 003 is Start ****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search box text field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_add_to_cart_button_on_product_in_search_result()
        self.logger.info("Clicking on the add to cart button")
        self.logger.info("**************************** Verifying Test Add To Cart 003 ****************************")
        self.pc = ProductComparePage(self.driver)
        if self.pc.success_message().__contains__('Success: You have added iMac to your shopping cart!'):
            self.atc.click_on_cart_button_in_black_color_beside_of_search_icon()
            self.logger.info("Clicking on the cart button beside of search icon")
            self.atc.click_on_view_cart_option()
            self.logger.info("Clicking on the view cart option")
            if self.driver.title == "Shopping Cart":
                if self.atc.get_product_name() == "iMac":
                    assert True
                    self.logger.info("************** Test Add To Cart 003 is Passed **************")
                else:
                    self.logger.error("************** Test Add To Cart 003 is Failed **************")
                    assert False
            else:
                self.logger.error("************** Test Add To Cart 003 is Failed **************")
                assert False
        else:
            self.logger.error("************** Test Add To Cart 003 is Failed **************")
            assert False
        self.logger.info("**************************** End Of Test Add To Cart 003 ****************************")

    @pytest.mark.sanity
    def test_add_to_cart_004(self, setup):
        self.driver = setup
        self.logger.info("**************************** Test Add To Cart 004 is Start ****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search box text field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_add_to_cart_button_on_product_in_search_result()
        self.logger.info("Clicking on the add to cart button")
        self.logger.info("**************************** Verifying Test Add To Cart 004 ****************************")
        self.pc = ProductComparePage(self.driver)
        if self.pc.success_message().__contains__('Success: You have added iMac to your shopping cart!'):
            self.pc.click_on_shopping_cart_link()
            self.logger.info("Clicking on the sopping cart link")
            if self.driver.title == "Shopping Cart":
                if self.atc.get_product_name() == "iMac":
                    assert True
                    self.logger.info("************** Test Add To Cart 004 is Passed **************")
                else:
                    self.logger.error("************** Test Add To Cart 004 is Failed **************")
                    assert False
            else:
                self.logger.error("************** Test Add To Cart 004 is Failed **************")
                assert False
        else:
            self.logger.error("************** Test Add To Cart 004 is Failed **************")
            assert False
        self.logger.info("**************************** End Of Test Add To Cart 004 ****************************")

    @pytest.mark.sanity
    def test_add_to_cart_005(self, setup):
        self.driver = setup
        self.logger.info("******************************* Test Add To Cart 005 is Start *******************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(
        self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("Hovering on desktop option and Clicking on the all desktop option")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_mac_subcategory_option_from_the_left_side_options()
        self.logger.info("Clicking on the mac subcategory option")
        self.atc.click_on_add_to_cart_button_on_product_in_search_result()
        self.logger.info("Clicking on add to cart button")
        self.logger.info("******************************* Verifying Test Add To Cart 005 *******************************")
        if self.pc.success_message().__contains__('Success: You have added iMac to your shopping cart!'):
            self.logger.info("success message is passed")
            self.pc.click_on_shopping_cart_link()
            self.logger.info("Clicking on the shopping cart link")
            if self.atc.is_title_of_the_page("Shopping Cart"):
                self.logger.info("page title is Passed")
                if self.atc.get_product_name() == "iMac":
                    assert True
                    self.logger.info("***************** Test Add To Cart 005 is Passed ****************")
                else:
                    self.logger.error(f"{self.atc.get_product_name()}")
                    self.logger.error("***************** Test Add To Cart 005 is Failed ****************")
                    assert False
            else:
                self.logger.error("***************** Test Add To Cart 005 is Failed ****************")
                assert False
        else:
            self.logger.error("***************** Test Add To Cart 005 is Failed ****************")
            assert False
        self.logger.info("******************************* End Of Test Add To Cart 005 *******************************")

    @pytest.mark.sanity
    def test_add_to_cart_006(self, setup):
        self.driver = setup
        self.logger.info("**************************** Test Add To Cart 006 is Start ****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to base url")
        self.atc = AddToCartPage(self.driver)
        self.atc.click_on_add_to_cart_button_on_featured_home_page()
        self.logger.info("Clicking on the add to cart button on featured home page ")
        self.logger.info("**************************** Verifying Test Add To Cart 006 ****************************")
        self.pc = ProductComparePage(self.driver)
        if self.pc.success_message().__contains__('Success: You have added MacBook to your shopping cart!'):
            self.pc.click_on_shopping_cart_link()
            self.logger.info("Clicking on the shopping cart link")
            if self.atc.is_title_of_the_page("Shopping Cart"):
                if self.atc.get_product_name() == "MacBook":
                    assert True
                    self.logger.info("***************** Test Add To Cart 006 is Passed ****************")
                else:
                    self.logger.error("***************** Test Add To Cart 006 is Failed ****************")
                    assert False
            else:
                self.logger.error("***************** Test Add To Cart 006 is Failed ****************")
                assert False
        else:
            self.logger.error("***************** Test Add To Cart 006 is Failed ****************")
            assert False
        self.logger.info("**************************** End Of Test Add To Cart 006 ****************************")

    @pytest.mark.sanity
    def test_add_to_cart_007(self, setup):
        self.driver = setup
        self.logger.info("**************************** Test Add To Cart 007 is Start ****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on compare this product option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on product comparison link")
        self.pc.click_on_add_to_cart_button()
        self.logger.info("Clicking on add to cart button")
        self.logger.info("**************************** Verifying Test Add To Cart 007 ****************************")
        if self.pc.success_message().__contains__('Success: You have added iMac to your shopping cart!'):
            self.pc.click_on_shopping_cart_link()
            self.logger.info("Clicking on shopping Cart link")
            self.atc = AddToCartPage(self.driver)
            if self.atc.is_title_of_the_page("Shopping Cart"):
                if self.atc.get_product_name() == "iMac":
                    assert True
                    self.logger.info("**************** Test Add To Cart 007 is Passed *****************")
                else:
                    self.logger.error("**************** Test Add To Cart 007 is Failed *****************")
                    assert False
            else:
                self.logger.error("**************** Test Add To Cart 007 is Failed *****************")
                assert False
        else:
            self.logger.error("**************** Test Add To Cart 007 is Failed *****************")
            assert False
        self.logger.info("**************************** End Of Test Add To Cart 007 ****************************")

    @pytest.mark.sanity
    def test_add_to_cart_008(self, setup):
        self.logger.info("*************************** Test Add To Cart 008 is Start ***************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on product display in search result")
        add_to_cart_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='button-cart']"))
        )
        self.logger.info("*************************** Verifying Test Add To Cart 008 ***************************")
        if add_to_cart_button.is_displayed() and add_to_cart_button.is_enabled():
            actions = ActionChains(self.driver)
            actions.move_to_element(add_to_cart_button).perform()
            add_to_cart_button.click()
            self.logger.info("Clicking on the add to cart button")
            if self.pc.success_message().__contains__('Success: You have added iMac to your shopping cart!'):
                self.pc.click_on_shopping_cart_link()
                self.logger.info("Clicking on the shopping cart link")
                self.atc = AddToCartPage(self.driver)
                if self.atc.is_title_of_the_page("Shopping Cart"):
                    if self.atc.get_product_name() == "iMac":
                        assert True
                        self.logger.info("************** Test Add To Cart 008 is Passed *************")
                    else:
                        self.logger.error("************** Test Add To Cart 008 is Failed *************")
                        assert False
                else:
                    self.logger.error("************** Test Add To Cart 008 is Failed *************")
                    assert False
            else:
                self.logger.error("************** Test Add To Cart 008 is Failed *************")
                assert False
            self.logger.info("*************************** End Of Test Add To Cart 008 ***************************")




        






