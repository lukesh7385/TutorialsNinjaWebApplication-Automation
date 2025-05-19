import pytest
from selenium.webdriver.common.by import By
from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.ProductDisplayPage import ProductDisplayPage
from pageObjects.SearchPage import SearchPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

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
        self.pc.click_on_imac_product()
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
        self.pc.click_on_imac_product()
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
        self.pc.click_on_imac_product()
        self.logger.info("Clicking on the product display in the search result")
        availability_status = self.driver.find_element(By.XPATH, "//li[normalize-space()='Availability:Out Of Stock']").text
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
        self.pc.click_on_imac_product()
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








