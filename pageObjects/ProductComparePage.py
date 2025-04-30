from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ProductComparePage:
    iMacProduct = (By.XPATH, "//img[@title='iMac']")
    compareThisProductOption = (By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/button[2]")
    compareThisProductOptionOnProduct = (By.XPATH, "//button[3][contains(@data-original-title,'Compare this Product')]")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    linkProductComparison = (By.XPATH, "//a[2]")
    btnListView = (By.XPATH, "//i[@class='fa fa-th-list']")
    btnGridView = (By.XPATH, "//button[@id='grid-view']")
    desktopsOption = (By.LINK_TEXT, "Desktops")
    showAllDesktopsOption = (By.XPATH, "//a[normalize-space()='Show AllDesktops']")
    compareThisProductOptionOnHomePage = (By.XPATH, "//div[@id='content']//div[1]//div[1]//div[3]//button[3]")
    productCompareLinkOnSearchResultPage = (By.LINK_TEXT, "Product Compare (0)")


    def __init__(self, driver):
        self.driver = driver

    def click_on_imac_product(self):
        self.driver.find_element(*ProductComparePage.iMacProduct).click()

    def click_on_compare_this_product_option(self):
        self.driver.find_element(*ProductComparePage.compareThisProductOption).click()

    def success_message(self):
        success_message = self.driver.find_element(*ProductComparePage.successMessage).text
        return success_message

    def click_on_product_comparison_link(self):
        product_comparison_link = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(self.linkProductComparison)
        )
        product_comparison_link.click()

    def click_on_list_view_button(self):
        self.driver.find_element(*ProductComparePage.btnListView).click()

    def click_on_grid_view_button(self):
        self.driver.find_element(*ProductComparePage.btnGridView).click()

    def click_on_compare_this_product_option_available_on_the_product(self):
        self.driver.find_element(*ProductComparePage.compareThisProductOptionOnProduct).click()

    def hover_on_desktops_option(self):
        return self.driver.find_element(*ProductComparePage.desktopsOption)

    def clicking_on_show_all_desktops_option(self):
        return self.driver.find_element(*ProductComparePage.showAllDesktopsOption)

    def click_on_compare_this_option_of_product_displayed_in_the_featured_section_of_home_page(self):
        self.driver.find_element(*ProductComparePage.compareThisProductOptionOnHomePage).click()

    def click_on_product_compare_link_on_search_result_page(self):
        self.driver.find_element(*ProductComparePage.productCompareLinkOnSearchResultPage).click()


