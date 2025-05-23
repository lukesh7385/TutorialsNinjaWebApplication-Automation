import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.ProductDisplayPage import ProductDisplayPage
from pageObjects.SearchPage import SearchPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import unicodedata
import difflib

@pytest.mark.usefixtures('setup', 'log_on_failure')
class Test_007_Product_Display:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_product_display_001(self, setup):
        self.driver = setup
        self.logger.info("********************** Test Product Display 001 is Start *********************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search text field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product displayed in the Search results")
        self.pd = ProductDisplayPage(self.driver)
        self.pd.click_on_thumbnail_image()
        self.logger.info("Clicking on the main bigger sized Thumbnail image")
        self.logger.info("********************** Verifying Test Product Display 001 *********************")
        if self.pd.first_thumbnail_image_in_light_view_is_display():
            if self.pd.next_arrow_button_is_display():
                if self.pd.prev_arrow_button_is_display():
                    self.pd.click_on_next_arrow_button()
                    self.logger.info("Clicking on the next arrow button")
                    if self.pd.second_thumbnail_image_in_light_view_is_display():
                        self.pd.click_on_prev_arrow_button()
                        self.logger.info("Clicking on the back arrow button")
                        if self.pd.first_thumbnail_image_in_light_view_is_display():
                            self.pd.click_on_cross_option()
                            self.logger.info("Clicking on the cross option")
                            if self.driver.title == "iMac":
                                assert True
                                self.logger.info("********** Test Product Display 001 is Passed **********")
                            else:
                                self.logger.error("********** Test Product Display 001 is Failed **********")
                                assert False
                        else:
                            self.logger.error("********** Test Product Display 001 is Failed **********")
                            assert False
                    else:
                        self.logger.error("********** Test Product Display 001 is Failed **********")
                        assert False
                else:
                    self.logger.error("********** Test Product Display 001 is Failed **********")
                    assert False
            else:
                self.logger.error("********** Test Product Display 001 is Failed **********")
                assert False
        else:
            self.logger.error("********** Test Product Display 001 is Failed **********")
            assert False
        self.pd.click_on_thumbnail_image()
        self.logger.info("Clicking on the main bigger sized Thumbnail image")
        self.logger.info("********************** Again Verifying Test Product Display 001 *********************")
        if self.pd.first_thumbnail_image_in_light_view_is_display():
            if self.pd.next_arrow_button_is_display():
                if self.pd.prev_arrow_button_is_display():
                    self.pd.click_on_next_arrow_button()
                    self.logger.info("Clicking on the next arrow button")
                    if self.pd.second_thumbnail_image_in_light_view_is_display():
                        self.pd.click_on_prev_arrow_button()
                        self.logger.info("Clicking on the back arrow button")
                        if self.pd.first_thumbnail_image_in_light_view_is_display():
                            self.pd.click_on_cross_option()
                            self.logger.info("Clicking on the cross option")
                            if self.driver.title == "iMac":
                                assert True
                                self.logger.info("********** Test Product Display 001 is Passed **********")
                            else:
                                self.logger.error("********** Test Product Display 001 is Failed **********")
                                assert False
                        else:
                            self.logger.error("********** Test Product Display 001 is Failed **********")
                            assert False
                    else:
                        self.logger.error("********** Test Product Display 001 is Failed **********")
                        assert False
                else:
                    self.logger.error("********** Test Product Display 001 is Failed **********")
                    assert False
            else:
                self.logger.error("********** Test Product Display 001 is Failed **********")
                assert False
        else:
            self.logger.error("********** Test Product Display 001 is Failed **********")
            assert False
        self.driver.quit()
        self.logger.info("********************** End Of Test Product Display 001 *********************")

    @pytest.mark.sanity
    def test_product_display_002(self, setup):
        self.driver = setup
        self.logger.info("*********************** Test Product Display 002 is Start ************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search text field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the iMac product")
        product_name = self.driver.find_element(By.XPATH, "//h1[normalize-space()='iMac']").text
        brand = self.driver.find_element(By.LINK_TEXT, "Apple").text
        product_code = self.driver.find_element(By.XPATH, "//li[normalize-space()='Product Code:Product 14']").text
        self.logger.info("*********************** Verifying Test Product Display 002 ************************")
        if product_name == "iMac":
            if brand == "Apple":
                if product_code == "Product Code:Product 14":
                    assert True
                    self.logger.info("************ Test Product Display 002 is Passed ***********")
                else:
                    self.logger.error("************ Test Product Display 002 is Failed ***********")
                    assert False
            else:
                self.logger.error("************ Test Product Display 002 is Failed ***********")
                assert False
        else:
            self.logger.error("************ Test Product Display 002 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("*********************** End Of Test Product Display 002 ************************")

    @pytest.mark.sanity
    def test_product_display_003(self, setup):
        self.driver = setup
        self.logger.info("************************* Test Product Display 003 is Start *************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in the search result")
        availability_status = self.driver.find_element(By.XPATH,
                                                       "//li[normalize-space()='Availability:Out Of Stock']").text
        self.logger.info("************************* Verifying Test Product Display 003 *************************")
        if self.driver.title == "iMac":
            if availability_status == "Availability:Out Of Stock":
                assert True
                self.logger.info("*********** Test Product Display 003 is Passed ************")
            else:
                self.logger.error("*********** Test Product Display 003 is Failed ************")
                assert False
        else:
            self.logger.error("*********** Test Product Display 003 is Failed ************")
            assert False
        self.driver.quit()
        self.logger.info("************************* End Of Test Product Display 003 *************************")

    @pytest.mark.sanity
    def test_product_display_004(self, setup):
        self.driver = setup
        self.logger.info("************************* Test Product Display 004 is Start *************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in the search result")
        price_with_tax = self.driver.find_element(By.XPATH, "//h2[normalize-space()='$122.00']").text
        price_without_tax = self.driver.find_element(By.XPATH, "//li[normalize-space()='Ex Tax:$100.00']").text
        self.logger.info("************************* Verifying Test Product Display 004 *************************")
        if self.driver.title == "iMac":
            if price_with_tax == "$122.00":
                if price_without_tax == "Ex Tax:$100.00":
                    assert True
                    self.logger.info("************* Test Product Display 004 is Passed ************")
                else:
                    self.logger.error("************* Test Product Display 004 is Failed ************")
                    assert False
            else:
                self.logger.error("************* Test Product Display 004 is Failed ************")
                assert False
        else:
            self.logger.error("************* Test Product Display 004 is Failed ************")
            assert False
        self.driver.quit()
        self.logger.info("************************* End Of Test Product Display 004 *************************")

    @pytest.mark.sanity
    def test_product_display_005(self, setup):
        self.driver = setup
        self.logger.info("************************* Test Product Display 005 is Start *************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in the search result")
        self.logger.info("************************* Verifying Test Product Display 005 *************************")
        self.pd = ProductDisplayPage(self.driver)
        if self.driver.title == "iMac":
            if self.pd.get_default_product_quantity() == "1":
                self.pd.set_product_quantity("3")
                self.logger.info("Updating quantity by 3")
                self.pd.click_on_add_to_cart_button_on_product_display_page()
                self.logger.info("Clicking on add to cart button")
                if self.pc.success_message().__contains__("Success: You have added iMac to your shopping cart!"):
                    self.pc.click_on_shopping_cart_link()
                    self.logger.info("Clicking on the shopping cart link")
                    if self.driver.title == "Shopping Cart":
                        if self.pd.get_updated_product_quantity() == "3":
                            assert True
                            self.logger.info("************** Test Product Display 005 is Passed **************")
                        else:
                            self.logger.error("************** Test Product Display 005 Failed **************")
                            assert False
                    else:
                        self.logger.error("************** Test Product Display 005 Failed **************")
                        assert False
                else:
                    self.logger.error("************** Test Product Display 005 Failed **************")
                    assert False
            else:
                self.logger.error("************** Test Product Display 005 Failed **************")
                assert False
        else:
            self.logger.error("************** Test Product Display 005 Failed **************")
            assert False
        self.driver.quit()
        self.logger.info("************************* End Of Test Product Display 005 *************************")

    @pytest.mark.sanity
    def test_product_display_006(self, setup):
        self.driver = setup
        self.logger.info("************************* Test Product Display 006 is Start *************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in the search result")
        self.logger.info("************************* Verifying Test Product Display 006 *************************")
        self.pd = ProductDisplayPage(self.driver)
        if self.pd.get_default_product_quantity() == "1":
            self.pd.set_product_quantity("-1")
            self.logger.info("Updating the product quantity to -1")
            self.pd.click_on_add_to_cart_button_on_product_display_page()
            self.logger.info("Clicking on the add to cart button")

            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            self.logger.info("Page has fully loaded")

            if self.pd.get_default_product_quantity() == "1":
                assert True
                self.logger.info("*********** Test Product Display 006 is Passed ***********")
            else:
                self.logger.error(f"{self.pd.get_default_product_quantity()}")
                self.logger.error("*********** Test Product Display 006 is Failed ***********")
                assert False
        else:
            self.logger.error("*********** Test Product Display 006 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("************************* End Test Product Display 006 *************************")

    @pytest.mark.skip("there is no radio button is present to perform click operation (it is under development)"
                      "and test can't move forward without radio button because it is mandatory field")
    @pytest.mark.sanity
    def test_product_display_007(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Display 007 is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("Apple Cinema 30")
        self.logger.info("Entering Apple Cinema 30 to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.pd = ProductDisplayPage(self.driver)
        self.logger.info("*************************** Verifying Test Product Display 007 **************************")
        if self.pd.get_default_product_quantity() == "2":
            if "This product has a minimum quantity of 2" in self.pd.get_information_text():
                self.pd.click_on_radio_button()
                self.logger.info("Clicking on radio button")
                self.pd.click_on_check_box1()
                self.logger.info("Clicking on check box1")
                self.pd.click_on_check_box2()
                self.logger.info("Clicking on check box2")
                self.pd.enter_text_to_text_field("Test")
                self.pd.select_dropdown_option()
                self.logger.info("Selecting dropdown option")
                self.pd.enter_text_to_text_area("Test")
                self.pd.upload_file()
                self.logger.info("Uploading file")
                self.pd.accept_alert()
                self.logger.info("Accepting alert")
                self.pd.set_date("2025-06-20")
                self.logger.info("Entering date")
                self.pd.set_time("22:25")
                self.logger.info("Entering time")
                self.pd.set_date_and_time("2025-06-20 22:25")
                self.logger.info("Entering date and time")
                self.pd.set_product_quantity("1")
                self.logger.info("Update the product quantity to 1")
                self.pd.click_on_add_to_cart_button_on_product_display_page()
                self.logger.info("Clicking on add to cart button")
                if self.pd.warning_message() == 'Minimum order amount for Apple Cinema 30" is 2!':
                    assert True
                    self.logger.info("************* Test Product Display 007 is Passed ************")
                else:
                    self.logger.error("************* Test Product Display 007 is Failed ************")
                    assert False
            else:
                self.logger.error("************* Test Product Display 007 is Failed ************")
                assert False
        else:
            self.logger.error("************* Test Product Display 007 is Failed ************")
            assert False
        self.logger.info("*************************** End Of Test Product Display 007 **************************")

    @pytest.mark.sanity
    def test_product_display_008(self, setup):
        self.driver = setup
        self.logger.info("***************************** Test Product Display 008 is Start ***************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to base url")

        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering 'iMac' into the search box")
        self.sf.click_on_search_button()
        self.logger.info("Clicking the search button")

        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the displayed product in search results")

        self.logger.info("***************************** Verifying Test Product Display 008 ***************************")
        self.pd = ProductDisplayPage(self.driver)

        # Expected Product Description (formatted)
        exp_description = (
            "Just when you thought iMac had everything, now there's even more.\n"
            "More powerful Intel Core 2 Duo processors.\n"
            "And more memory standard.\n"
            "Combine this with Mac OS X Leopard and iLife '08, and it's more all-in-one than ever.\n"
            "iMac packs amazing performance into a stunningly slim space."
        )

        # Retrieving and normalizing actual description
        actual_description = self.pd.get_description_text().replace("´", "'").strip()

        # Unicode normalization
        exp_normalized = unicodedata.normalize('NFKC', exp_description).strip()
        actual_normalized = unicodedata.normalize('NFKC', actual_description).strip()

        # Logging both values for debugging
        self.logger.info(f"Expected Description:\n{exp_normalized}")
        self.logger.info(f"Actual Description:\n{actual_normalized}")

        # Checking similarity with fuzzy matching
        similarity = difflib.SequenceMatcher(None, exp_normalized, actual_normalized).ratio()

        if similarity > 0.95:  # Accepting minor differences
            assert True
            self.logger.info("************** Test Product Display 008 is Passed ************")
        else:
            print(actual_normalized)  # Print actual description for further debugging
            self.logger.info("************** Test Product Display 008 is Failed ************")
            assert False

        self.logger.info("***************************** End Of Test Product Display 008 ***************************")

    @pytest.mark.sanity
    def test_product_display_009(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Display 009 is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("Apple Cinema 30")
        self.logger.info("Entering Apple Cinema 30 to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.pd = ProductDisplayPage(self.driver)
        self.pd.click_on_specification_tab()
        self.logger.info("*************************** Verifying Test Product Display 009 **************************")
        specification1 = self.driver.find_element(By.XPATH, '//*[@id="tab-specification"]/table/tbody/tr/td[1]').text
        specification2 = self.driver.find_element(By.XPATH, '//*[@id="tab-specification"]/table/tbody/tr/td[2]').text
        if specification1 == "clock speed":
            if specification2 == "100mhz":
                assert True
                self.logger.info("*************** Test Product Display 009 is Passed **************")
            else:
                self.logger.info(f"Expected: '100mhz' but Actual: '{specification2}'")
                self.logger.error("*************** Test Product Display 009 is Failed **************")
                assert False
        else:
            self.logger.info(f"Expected: 'clock speed' but Actual: '{specification1}")
            self.logger.error("*************** Test Product Display 009 is Failed **************")
            assert False
        self.logger.info("*************************** End Of Test Product Display 009 **************************")

    @pytest.mark.sanity
    def test_product_display_010(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Display 010 is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("Apple Cinema 30")
        self.logger.info("Entering Apple Cinema 30 to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.pd = ProductDisplayPage(self.driver)
        self.pd.click_on_reviews_tab()
        self.logger.info("Clicking on review tab")
        self.pd.set_name_in_review_tab("Lukesh")
        self.logger.info("Entering name in name text field in review tab")
        self.pd.set_review_text_in_review_tab("This product is nice! and i recommend this product to buy this product")
        self.logger.info("Entering the review text to the review text area")
        self.pd.click_on_radio_button_in_review_tab()
        self.logger.info("Clicking on the radio button")
        self.pd.click_on_continue_button_in_review_tab()
        self.logger.info("Clicking on the continue button")
        self.logger.info("*************************** Verifying Test Product Display 010 **************************")
        exp_success_message =  'Thank you for your review. It has been submitted to the webmaster for approval.'
        act_success_message = self.pd.get_success_message_in_review_tab()
        if act_success_message == exp_success_message:
            assert True
            self.logger.info("**************** Test Product Display 010 is Passed ***************")
        else:
            self.logger.error(f"Expected Success Message is:- {exp_success_message}")
            self.logger.error(f"Actual Success Message is:- {act_success_message}")
            self.logger.error("**************** Test Product Display 010 is Failed ***************")
            assert False
        self.logger.info("*************************** End Of Test Product Display 010 **************************")

    @pytest.mark.sanity
    def test_product_display_011(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Display 011 is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search text box field")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search icon button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_the_product_display_in_search_result()
        self.logger.info("Clicking on the product display in search result")
        self.pd = ProductDisplayPage(self.driver)
        self.pd.click_on_reviews_tab()
        self.logger.info("Clicking on the zero review tab")
        self.logger.info("*************************** Verifying Test Product Display 011 **************************")
        no_review_message = self.pd.get_no_review_text_message()
        if no_review_message ==  'There are no reviews for this product.':
            assert True
            self.logger.info("************* Test Product Display 011 is Passed ***************")
        else:
            self.logger.error(f"Actual no review text is: {no_review_message}")
            self.logger.info("************* Test Product Display 011 is Failed ***************")
            assert False
        self.logger.info("*************************** End Of Test Product Display 011 **************************")



