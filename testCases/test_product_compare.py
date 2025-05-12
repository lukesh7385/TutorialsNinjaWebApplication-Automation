import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.ProductComparePage import ProductComparePage
from pageObjects.SearchPage import SearchPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures('setup', 'log_on_failure')
class Test_006_Product_Compare:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_product_compare_001(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 001 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.sp = SearchPage(self.driver)
        self.sp.search_product("iMac")
        self.logger.info("Entering iMac product for search")
        self.sp.click_on_search_button()
        self.logger.info("clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_imac_product()
        self.logger.info("Clicking on the Product displayed in the Search results")
        self.logger.info("*************** Verifying Test Product Compare 001 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                      "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/button[2]")
        if self.tooltip_text.get_attribute("data-original-title")== "Compare this Product":
            self.pc.click_on_compare_this_product_option()
            self.logger.info("clicking on compare this product option")
            if self.pc.success_message().__contains__("Success: You have added iMac to your product comparison!"):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 001 is Passed ***********")
                else:
                    self.logger.error("********** Test Product Compare 001 is Failed ***********")
                    assert False
            else:
                self.logger.error("********** Test Product Compare 001 is Failed ***********")
                assert False
        else:
            self.logger.error("********** Test Product Compare 001 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 001 *************************")

    @pytest.mark.sanity
    def test_product_compare_002(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 002 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.sp = SearchPage(self.driver)
        self.sp.search_product("iMac")
        self.logger.info("Entering iMac product for search")
        self.sp.click_on_search_button()
        self.logger.info("clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_list_view_button()
        self.logger.info("Clicking on list view button")
        self.logger.info("*************** Verifying Test Product Compare 002 ****************")

        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//button[3][contains(@data-original-title,'Compare this Product')]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.click_on_compare_this_product_option_available_on_the_product()
            self.logger.info("clicking on compare this product option available on the Product that is displayed in the Search")
            if self.pc.success_message().__contains__("Success: You have added iMac to your product comparison!"):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 002 is Passed ***********")
                else:
                    self.logger.error("********** Test Product Compare 002 is Failed ***********")
                    assert False
            else:
                self.logger.error("********** Test Product Compare 002 is Failed ***********")
                assert False
        else:
            print(self.tooltip_text.get_attribute("data-original-title"))
            self.logger.error("********** Test Product Compare 002 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 002 *************************")

    @pytest.mark.sanity
    def test_product_compare_003(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 003 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.sp = SearchPage(self.driver)
        self.sp.search_product("iMac")
        self.logger.info("Entering iMac product for search")
        self.sp.click_on_search_button()
        self.logger.info("clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_grid_view_button()
        self.logger.info("Clicking on grid view button")
        self.logger.info("*************** Verifying Test Product Compare 003 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//button[3][contains(@data-original-title,'Compare this Product')]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.click_on_compare_this_product_option_available_on_the_product()
            self.logger.info("clicking on compare this product option available on the Product that is displayed in the Search")
            if self.pc.success_message().__contains__("Success: You have added iMac to your product comparison!"):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                time.sleep(1)
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 003 is Passed ***********")
                else:
                    self.logger.error("********** Test Product Compare 003 is Failed ***********")
                    assert False
            else:
                self.logger.error("********** Test Product Compare 003 is Failed ***********")
                assert False
        else:
            print(self.tooltip_text.get_attribute("data-original-title"))
            self.logger.error("********** Test Product Compare 003 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 003 *************************")

    @pytest.mark.sanity
    def test_product_compare_004(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 004 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("hovering on desktops option and clicking on show all desktops option")
        self.pc.click_on_list_view_button()
        self.logger.info("Clicking on list view button")
        self.logger.info("*************** Verifying Test Product Compare 004 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//*[@id='content']/div[4]/div[1]/div/div[2]/div[2]/button[3]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.click_on_compare_this_product_option_available_on_the_product()
            self.logger.info(
                "clicking on compare this product option available on the Product that is displayed in the Product Category page")
            if self.pc.success_message().__contains__('Success: You have added Apple Cinema 30" to your product comparison!'):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 004 is Passed ***********")
                else:
                    self.logger.info(f"{self.driver.title}")
                    self.logger.error("********** Test Product Compare 004 is Failed ***********")
                    assert False
            else:
                self.logger.info(f"{self.pc.success_message()}")
                self.logger.error("********** Test Product Compare 004 is Failed ***********")
                assert False
        else:
            self.logger.info(f"{self.tooltip_text.get_attribute("data-original-title")}")
            self.logger.error("********** Test Product Compare 004 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 004 *************************")

    @pytest.mark.sanity
    def test_product_compare_005(self, setup):
        self.driver = setup
        self.logger.info("***************** Test Product Compare 005 Is Start *****************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(
            self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("hovering on desktops option and clicking on show all desktops option")
        self.pc.click_on_grid_view_button()
        self.logger.info("Clicking on grid view button")
        self.logger.info("*************** Verifying Test Product Compare 005 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//*[@id='content']/div[4]/div[1]/div/div[2]/div[2]/button[3]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.click_on_compare_this_product_option_available_on_the_product()
            self.logger.info(
                "clicking on compare this product option available on the Product that is displayed in the Product Category page")
            if self.pc.success_message().__contains__(
                    'Success: You have added Apple Cinema 30" to your product comparison!'):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 005 is Passed ***********")
                else:
                    self.logger.info(f"{self.driver.title}")
                    self.logger.error("********** Test Product Compare 005 is Failed ***********")
                    assert False
            else:
                self.logger.info(f"{self.pc.success_message()}")
                self.logger.error("********** Test Product Compare 005 is Failed ***********")
                assert False
        else:
            self.logger.info(f"{self.tooltip_text.get_attribute("data-original-title")}")
            self.logger.error("********** Test Product Compare 005 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 005 *************************")

    @pytest.mark.sanity
    def test_product_compare_006(self, setup):
        self.driver = setup
        self.logger.info("****************** Test Product Compare 006 Is Starting *********************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to base url")
        self.sp = SearchPage(self.driver)
        self.sp.search_product("iMac")
        self.logger.info("Entering iMac product to search")
        self.sp.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_imac_product()
        self.logger.info("Click on the iMac Product displayed in the Search results ")
        self.logger.info("*************** Verifying Test Product Compare 006 ****************")
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/button[2]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.click_on_compare_this_product_option()
            self.logger.info(
                "clicking on compare this product option available on the Product that is displayed in the Product Category page")
            if self.pc.success_message().__contains__('Success: You have added iMac to your product comparison!'):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 006 is Passed ***********")
                else:
                    self.logger.info(f"{self.driver.title}")
                    self.logger.error("********** Test Product Compare 006 is Failed ***********")
                    assert False
            else:
                self.logger.info(f"{self.pc.success_message()}")
                self.logger.error("********** Test Product Compare 006 is Failed ***********")
                assert False
        else:
            self.logger.info(f"{self.tooltip_text.get_attribute("data-original-title")}")
            self.logger.error("********** Test Product Compare 006 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 006 *************************")

    @pytest.mark.sanity
    def test_product_compare_007(self, setup):
        self.driver = setup
        self.logger.info("******************* Test Product Compare 007 Is Start ********************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.logger.info("*************** Verifying Test Product Compare 007 ****************")
        self.pc = ProductComparePage(self.driver)
        self.tooltip_text = self.driver.find_element(By.XPATH,
                                                     "//div[@id='content']//div[1]//div[1]//div[3]//button[3]")
        if self.tooltip_text.get_attribute("data-original-title") == "Compare this Product":
            self.pc.click_on_compare_this_option_of_product_displayed_in_the_featured_section_of_home_page()
            self.logger.info(
                "clicking on compare this product option available on the Product that is displayed in the Product Category page")
            time.sleep(1)
            if self.pc.success_message().__contains__('Success: You have added MacBook to your product comparison!'):
                self.pc.click_on_product_comparison_link()
                self.logger.info("clicking on product comparison link")
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("*********** Test Product Compare 007 is Passed ***********")
                else:
                    self.logger.info(f"{self.driver.title}")
                    self.logger.error("********** Test Product Compare 007 is Failed ***********")
                    assert False
            else:
                self.logger.info(f"{self.pc.success_message()}")
                self.logger.error("********** Test Product Compare 007 is Failed ***********")
                assert False
        else:
            self.logger.info(f"{self.tooltip_text.get_attribute("data-original-title")}")
            self.logger.error("********** Test Product Compare 007 is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************* End Test Product Compare 007 *************************")

    @pytest.mark.sanity
    def test_product_compare_008(self, setup):
        self.driver = setup
        self.logger.info("******************** Test Product Compare 008 Is Start ********************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_product_compare_link_on_search_result_page()
        self.logger.info("Clicking on product compare link on search result page")
        self.logger.info("*************** Verifying Test Product Compare 008 ***************")
        if self.driver.title == "Product Comparison":
            assert True
            self.logger.info("************ Test Product Compare 008 Is Passed ***********")
        else:
            self.logger.error("************ Test Product Compare 008 Is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("********************** End of Test Product Compare 008 ***********************")

    @pytest.mark.sanity
    def test_product_compare_009(self, setup):
        self.driver = setup
        self.logger.info("******************** Test Product Compare 009 Is Start ********************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(
            self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("Hovering mouse on desktop option and Clicking on show all desktop option")
        self.pc.click_on_product_compare_link_on_search_result_page()
        self.logger.info("Clicking on product compare link on search result page")
        self.logger.info("******************* Verifying Test Product Compare 009 *********************")
        if self.driver.title == "Product Comparison":
            assert True
            self.logger.info("*********** Test Product Compare 009 Is Passed ***********")
        else:
            self.logger.error("*********** Test Product Compare 009 Is Failed ***********")
            assert False
        self.driver.quit()
        self.logger.info("*********************** End Of Test Product Compare 009 *************************")

    @pytest.mark.sanity
    def test_product_compare_010(self, setup):
        self.driver = setup
        self.logger.info("******************** Test Product Compare 010 Is Start ********************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(
            self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("Hovering mouse on desktop option and Clicking on show all desktop option")
        self.pc.click_on_product_compare_link_on_search_result_page()
        self.logger.info("Clicking on product compare link on search result page")
        self.logger.info("******************* Verifying Test Product Compare 010 *********************")
        self.textMessage = self.driver.find_element(By.XPATH, "//p[normalize-space()='You have not chosen any products to compare.']").text
        if self.textMessage == "You have not chosen any products to compare.":
            assert True
            self.logger.info("********** Test Product Compare 010 is Passed **********")
        else:
            self.logger.info("********** Test Product Compare 010 is Failed **********")
            assert False
        self.driver.quit()
        self.logger.info("******************** End Test Product Compare 010 ************************")

    @pytest.mark.sanity
    def test_product_compare_011(self, setup):
        self.driver = setup
        self.logger.info("************************** Test Product Compare 011 Is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(
            self.pc.clicking_on_show_all_desktops_option()).click().perform()
        self.logger.info("Hovering on the desktop option and clicking on the show all desktop option")
        self.pc.click_on_product_compare_link_on_search_result_page()
        self.logger.info("Clicking on the product compare link on search result page")
        self.pc.click_on_continue_button()
        self.logger.info("Clicking on the Continue button")
        self.logger.info("********************** Verifying Test Product Compare 011 **************************")
        if self.driver.title == "Your Store":
            assert True
            self.logger.info("*********** Test Product Compare 011 Is Passed ***********")
        else:
            self.logger.error("************ Test Product Compare 011 Is Failed *************")
            assert False
        self.driver.quit()
        self.logger.info("*********************** End Test Product Compare 011 ***********************")

    @pytest.mark.sanity
    def test_product_compare_012(self, setup):
        self.driver = setup
        self.logger.info("************************ Test Product Compare 012 Is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.pc = ProductComparePage(self.driver)
        act = ActionChains(self.driver)
        act.move_to_element(self.pc.hover_on_desktops_option()).move_to_element(
            self.pc.clicking_on_show_all_desktops_option()
        ).click().perform()
        self.logger.info("Hovering on the desktop option and Clicking on the show all desktop option")
        self.pc.click_on_product_compare_link_on_search_result_page()
        self.logger.info("Clicking on the product compare link on the search result page")
        self.logger.info("************************* Verifying Test Product Compare 012 ****************************")
        if self.driver.title == "Product Comparison":
            self.pc.click_on_home_page_link_on_breadcrumb()
            self.logger.info("Clicking on the home page link available on the breadcrumb")
            WebDriverWait(self.driver, 10, poll_frequency=2).until(lambda driver: "Your Store" in driver.title)
            if self.driver.title == "Your Store":
                assert True
                self.logger.error("********** Test Product Compare 012 Is Passed **********")
            else:
                self.logger.error("********** Test Product Compare 012 Is Failed **********")
                assert False
        else:
            self.logger.info("********** Test Product Compare 012 Is Failed **********")
            assert False
        self.driver.quit()
        self.logger.info("************************ End Of Test Product Compare 012 **************************")

    @pytest.mark.sanity
    def test_product_compare_013(self, setup):
        self.driver = setup
        self.logger.info("**************************** Test Product Compare 013 ***************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering product iMac to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_imac_product()
        self.logger.info("Clicking on product displayed in the search result")
        self.pc.click_on_compare_this_product_option()
        self.logger.info("Clicking on the compare this product option")
        self.logger.info("********************** Verifying Test Product Compare 013 ************************")
        if self.pc.success_message().__contains__("Success: You have added iMac to your product comparison!"):
            self.pc.click_on_imac_product_on_success_message()
            WebDriverWait(self.driver, 10, poll_frequency=2).until(EC.title_is("iMac"))
            if self.driver.title == "iMac":
                self.pc.click_on_compare_this_product_option()
                self.logger.info("Clicking on the compare this product option")
                self.pc.click_on_product_comparison_link()
                self.logger.info("Clicking on the product comparison link")
                WebDriverWait(self.driver, 10, poll_frequency=2).until(EC.title_is("Product Comparison"))
                if self.driver.title == "Product Comparison":
                    assert True
                    self.logger.info("********** Test Product Compare 013 is Passed *********")
                else:
                    self.logger.error("********** Test Product Compare 013 is Failed *********")
                    assert False
            else:
                self.logger.error("********** Test Product Compare 013 is Failed *********")
                assert False
        else:
            self.logger.error("********** Test Product Compare 013 is Failed *********")
            assert False
        self.driver.quit()
        self.logger.info("**************************** End Test Product Compare 013 ***************************")

    @pytest.mark.sanity
    def test_product_compare_014(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Compare 014 is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_imac_product()
        self.logger.info("Clicking on product displayed in the search result")
        self.pc.click_on_compare_this_product_option()
        self.logger.info("Clicking on compare this product option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on the product comparison link")
        self.logger.info("*************************** Verifying Test Product Compare 014 **************************")
        self.productName = self.driver.find_element(By.LINK_TEXT, 'iMac').text
        self.productPrice = self.driver.find_element(By.XPATH, "//td[normalize-space()='$122.00']").text
        self.productModel = self.driver.find_element(By.XPATH, "//td[normalize-space()='Product 14']").text
        self.productBrand = self.driver.find_element(By.XPATH, "//td[normalize-space()='Apple']").text
        self.productWeight = self.driver.find_element(By.XPATH, "//td[normalize-space()='5.00kg']").text
        self.removeButton = self.driver.find_element(By.XPATH, "//a[normalize-space()='Remove']")
        if self.productName == 'iMac':
            if self.productPrice == '$122.00':
                if self.productModel == 'Product 14':
                    if self.productBrand == 'Apple':
                        if self.productWeight == '5.00kg':
                            if self.pc.add_to_cart_button().is_displayed():
                                if self.pc.remove_button().is_displayed():
                                    assert True
                                else:
                                    self.logger.info("************ Test Product Compare 014 is Failed ***********")
                                    assert False
                            else:
                                self.logger.info("************ Test Product Compare 014 is Failed ***********")
                                assert False
                            self.logger.info("************ Test Product Compare 014 is Passed ***********")
                        else:
                            self.logger.info("************ Test Product Compare 014 is Failed ***********")
                            assert False
                    else:
                        self.logger.info("************ Test Product Compare 014 is Failed ***********")
                        assert False
                else:
                    self.logger.info("************ Test Product Compare 014 is Failed ***********")
                    assert False
            else:
                self.logger.info("************ Test Product Compare 014 is Failed ***********")
                assert False
        else:
            self.logger.info("************ Test Product Compare 014 is Failed ***********")
            assert False
        # time.sleep(1)
        self.driver.quit()
        self.logger.info("*************************** End Test Product Compare 014 **************************")

    @pytest.mark.sanity
    def test_product_compare_015(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Compare 015 is Start *****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on compare this product option")
        self.sf.search_product("iphone")
        self.logger.info("Entering iphone product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on compare this product option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on the product comparison link")

        self.logger.info("************************ Verifying Test Product Compare 015 ************************")

        self.cols = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr[1]/td"))
        self.rows = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr"))
        l1 = []
        valid_entries = ["iMac", "iPhone", "$122.00", "$123.20", "Product 14", "product 11", "Apple",
                         "Apple"]  # Define valid entries

        for r in range(1, self.rows + 1):
            for c in range(2, self.cols + 1):  # Ensure column indexing consistency
                xpath = f"//tbody[1]/tr[{r}]/td[{c}]"
                self.data = self.driver.find_element(By.XPATH, xpath)

                # Append only the valid text (filter out extra info)
                if self.data.text.strip() in valid_entries:
                    l1.append(self.data.text.strip())

        expected_values = ["iMac", "iPhone", "$122.00", "$123.20", "Product 14", "product 11", "Apple", "Apple"]

        if l1 == expected_values:
            print("expected list: ", l1)
            if self.pc.add_to_cart_button().is_displayed():
                if self.pc.remove_button().is_displayed():
                    self.logger.info("********* Test Product Compare 015 is Passed *********")
                    assert True
                else:
                    self.logger.info("********* Test Product Compare 015 is Failed *********")
            else:
                self.logger.info("********* Test Product Compare 015 is Failed *********")
        else:
            print(f"Mismatch: {l1}")
            self.logger.info("********* Test Product Compare 015 is Failed *********")
            assert False
        self.driver.quit()
        self.logger.info("*************************** End Test Product Compare 015 *****************************")

    @pytest.mark.sanity
    def test_product_compare_016(self, setup):
        self.driver = setup
        self.logger.info("************************** Test Product Compare 016 is Start **************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering the iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this product option")
        self.sf.search_product("iMac")
        self.logger.info("Entering the iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this product option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on the product comparison link")
        self.logger.info("************************** Verifying Test Product Compare 016 **************************")
        self.cols = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr[1]/td"))
        self.rows = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr"))
        l1 = []
        valid_entries =["iMac", "$122.00", "Product 14", "Apple"] # Define valid entries

        for r in range(1, self.rows + 1):
            for c in range(2, self.cols + 1):  # Ensure column indexing consistency
                xpath = f"//tbody[1]/tr[{r}]/td[{c}]"
                self.data = self.driver.find_element(By.XPATH, xpath)

                # Append only the valid text (filter out extra info)
                if self.data.text.strip() in valid_entries:
                    l1.append(self.data.text.strip())

        expected_values = ["iMac", "$122.00", "Product 14", "Apple"]

        if self.cols == 2:
            if l1 == expected_values:
                print("expected list: ", l1)
                if self.pc.add_to_cart_button().is_displayed():
                    if self.pc.remove_button().is_displayed():
                        self.logger.info("********* Test Product Compare 016 is Passed *********")
                        assert True
                    else:
                        self.logger.info("********* Test Product Compare 016 is Failed *********")
                        assert False
                else:
                    self.logger.info("********* Test Product Compare 016 is Failed *********")
                    assert False
            else:
                print(f"Mismatch: {l1}")
                self.logger.info("********* Test Product Compare 016 is Failed *********")
                assert False
        else:
            self.logger.info("********* Test Product Compare 016 is Failed *********")
            assert False
        self.driver.quit()
        self.logger.info("*************************** End Test Product Compare 016 *****************************")

    @pytest.mark.sanity
    def test_product_compare_017(self, setup):
        self.driver = setup
        self.logger.info("***************************** Test Product Compare 017 is Start ***************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("iphone")
        self.logger.info("Entering iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook Air")
        self.logger.info("Entering iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on the product comparison link")
        self.logger.info("***************************** Verifying Test Product Compare 017 ***************************")
        self.cols = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr[1]/td"))
        self.rows = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr"))
        l1 = []
        valid_entries = ["iMac", "iPhone", "MacBook Air", "$122.00", "$123.20",
                         "$1,202.00", "Product 14", "product 11", "Product 17", "Apple", "Apple", "Apple"]  # Define valid entries

        for r in range(1, self.rows + 1):
            for c in range(2, self.cols + 1):  # Ensure column indexing consistency
                xpath = f"//tbody[1]/tr[{r}]/td[{c}]"
                self.data = self.driver.find_element(By.XPATH, xpath)

                # Append only the valid text (filter out extra info)
                if self.data.text.strip() in valid_entries:
                    l1.append(self.data.text.strip())

        expected_values = ["iMac", "iPhone", "MacBook Air", "$122.00", "$123.20",
                         "$1,202.00", "Product 14", "product 11", "Product 17", "Apple", "Apple", "Apple"]

        if self.cols == 4:
            if l1 == expected_values:
                print("expected list: ", l1)
                if self.pc.add_to_cart_button().is_displayed():
                    if self.pc.remove_button().is_displayed():
                        self.logger.info("********* Test Product Compare 017 is Passed *********")
                        assert True
                    else:
                        self.logger.error("********* Test Product Compare 017 is Failed *********")
                        assert False
                else:
                    self.logger.error("********* Test Product Compare 017 is Failed *********")
                    assert False
            else:
                print(f"Mismatch: {l1}")
                self.logger.error("********* Test Product Compare 017 is Failed *********")
                assert False
        else:
            self.logger.error("********* Test Product Compare 017 is Failed *********")
            assert False
        self.driver.quit()
        self.logger.info("*************************** End Test Product Compare 017 *****************************")

    @pytest.mark.sanity
    def test_product_compare_018(self, setup):
        self.driver = setup
        self.logger.info("***************************** Test Product Compare 018 is Start ***************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("iphone")
        self.logger.info("Entering iphone product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook Air")
        self.logger.info("Entering MacBook Air product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook")
        self.logger.info("Entering MacBook product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on the product comparison link")
        self.logger.info("***************************** Verifying Test Product Compare 018 ***************************")
        self.cols = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr[1]/td"))
        self.rows = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr"))
        l1 = []
        valid_entries = ["iMac", "iPhone", "MacBook Air", "MacBook", "$122.00", "$123.20",
                         "$1,202.00", "$602.00", "Product 14", "product 11", "Product 17", "Product 16", "Apple", "Apple",
                         "Apple", "Apple"]  # Define valid entries

        for r in range(1, self.rows + 1):
            for c in range(2, self.cols + 1):  # Ensure column indexing consistency
                xpath = f"//tbody[1]/tr[{r}]/td[{c}]"
                self.data = self.driver.find_element(By.XPATH, xpath)

                # Append only the valid text (filter out extra info)
                if self.data.text.strip() in valid_entries:
                    l1.append(self.data.text.strip())

        expected_values = ["iMac", "iPhone", "MacBook Air", "MacBook", "$122.00", "$123.20",
                         "$1,202.00", "$602.00", "Product 14", "product 11", "Product 17", "Product 16", "Apple", "Apple",
                         "Apple", "Apple"]

        if self.cols == 5:
            if l1 == expected_values:
                print("expected list: ", l1)
                if self.pc.add_to_cart_button().is_displayed():
                    if self.pc.remove_button().is_displayed():
                        self.logger.info("********* Test Product Compare 018 is Passed *********")
                        assert True
                    else:
                        self.logger.error("********* Test Product Compare 018 is Failed *********")
                        assert False
                else:
                    self.logger.error("********* Test Product Compare 018 is Failed *********")
                    assert False
            else:
                print(f"Mismatch: {l1}")
                self.logger.error("********* Test Product Compare 018 is Failed *********")
                assert False
        else:
            self.logger.error("********* Test Product Compare 018 is Failed *********")
            assert False
        self.driver.quit()
        self.logger.info("*************************** End Test Product Compare 018 *****************************")

    @pytest.mark.sanity
    def test_product_compare_019(self, setup):
        self.driver = setup
        self.logger.info("***************************** Test Product Compare 019 is Start ***************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("iphone")
        self.logger.info("Entering iphone product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook Air")
        self.logger.info("Entering MacBook Air product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook")
        self.logger.info("Entering MacBook product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook Pro")
        self.logger.info("Entering MacBook Pro product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on the product comparison link")
        self.logger.info("***************************** Verifying Test Product Compare 019 ***************************")
        self.cols = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr[1]/td"))
        self.rows = len(self.driver.find_elements(By.XPATH, "//table/tbody[1]/tr"))
        l = []
        valid_entries =  ["iPhone", "MacBook Air", "MacBook", "MacBook Pro", "$123.20",
                           "$1,202.00", "$602.00", "$2,000.00", "product 11", "Product 17", "Product 16", "Product 18",
                           "Apple", "Apple", "Apple", "Apple"]  # Define valid entries

        for r in range(1, self.rows + 1):
            for c in range(2, self.cols + 1):  # Ensure column indexing consistency
                xpath = f"//tbody[1]/tr[{r}]/td[{c}]"
                self.data = self.driver.find_element(By.XPATH, xpath)

                # Append only the valid text (filter out extra info)
                if self.data.text.strip() in valid_entries:
                    l.append(self.data.text.strip())

        expected_values = ["iPhone", "MacBook Air", "MacBook", "MacBook Pro", "$123.20",
                           "$1,202.00", "$602.00", "$2,000.00", "product 11", "Product 17", "Product 16", "Product 18",
                           "Apple", "Apple", "Apple", "Apple"]

        if self.cols == 5:
            if l == expected_values:
                print("expected list: ", l)
                if self.pc.add_to_cart_button().is_displayed():
                    if self.pc.remove_button().is_displayed():
                        self.logger.info("********* Test Product Compare 019 is Passed *********")
                        assert True
                    else:
                        self.logger.error("********* Test Product Compare 019 is Failed *********")
                        assert False
                else:
                    self.logger.error("********* Test Product Compare 019 is Failed *********")
                    assert False
            else:
                print(f"Mismatch: {l}")
                self.logger.error("********* Test Product Compare 019 is Failed *********")
                assert False
        else:
            self.logger.error("********* Test Product Compare 019 is Failed *********")
            assert False
        self.driver.quit()
        self.logger.info("*************************** End Test Product Compare 019 *****************************")

    @pytest.mark.sanity
    def test_product_compare_020(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Compare 020 is Start *****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on compare this product option")
        self.sf.search_product("iphone")
        self.logger.info("Entering iphone product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook Air")
        self.logger.info("Entering MacBook Air product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook")
        self.logger.info("Entering MacBook product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on product comparison link")
        self.pc.click_on_add_to_cart_button()
        self.logger.info("Clicking on add to cart button")
        self.pc.click_on_shopping_cart_link()
        self.logger.info("Clicking on shopping cart link")
        self.logger.info("*************************** Verifying Test Product Compare 020 *****************************")
        product_name = self.driver.find_element(By.LINK_TEXT, "iMac").text
        try:
            if product_name == "iMac":
                if self.driver.title == "Shopping Cart":
                    self.logger.info("************ Test Product Compare 020 is Passed *************")
                    assert True
                else:
                    print(f"Actual title mismatch: {self.driver.title}")
                    self.logger.info("************ Test Product Compare 020 is Failed *************")
                    assert False
            else:
                self.logger.info("************ Test Product Compare 020 is Failed *************")
                assert False
        finally:
            self.driver.quit()
            self.logger.info("*************************** End Test Product Compare 020 *****************************")

    @pytest.mark.sanity
    def test_product_compare_021(self, setup):
        self.driver = setup
        self.logger.info("*************************** Test Product Compare 021 is Start *****************************")
        self.driver.get(self.baseURL)
        self.logger.info("Navigating to the base url")
        self.sf = SearchPage(self.driver)
        self.sf.search_product("iMac")
        self.logger.info("Entering iMac product to search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on search button")
        self.pc = ProductComparePage(self.driver)
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on compare this product option")
        self.sf.search_product("iphone")
        self.logger.info("Entering iphone product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook Air")
        self.logger.info("Entering MacBook Air product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.sf.search_product("MacBook")
        self.logger.info("Entering MacBook product to the search")
        self.sf.click_on_search_button()
        self.logger.info("Clicking on the search button")
        self.pc.click_on_compare_this_product_option_available_on_the_product()
        self.logger.info("Clicking on the compare this option")
        self.pc.click_on_product_comparison_link()
        self.logger.info("Clicking on product comparison link")
        self.logger.info("*************************** Verifying Test Product Compare 021 *****************************")
        if self.driver.title == "Product Comparison":
            self.logger.info("Title is Passed")
            self.pc.click_on_remove_button()
            if self.pc.success_message().__contains__("Success: You have modified your product comparison!"):
                self.logger.info("*********** Test Product Compare 021 is Passed ************")
                assert True
            else:
                self.logger.error(f"Success message after remove product: {self.pc.success_message()}")
                self.logger.error("*********** Test Product Compare 021 is Failed ************")
                assert False
        else:
            self.logger.error("*********** Test Product Compare 021 is Failed ************")
            assert False
        self.driver.quit()
        self.logger.info("*************************** End Of Test Product Compare 021 *****************************")











































