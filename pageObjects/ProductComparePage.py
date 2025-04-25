from selenium.webdriver.common.by import By

class ProductComparePage:
    iMacProduct = (By.XPATH, "//img[@title='iMac']")
    compareThisProductOption = (By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/button[2]")
    compareThisProductOptionOnProduct = (By.XPATH, "//button[3][contains(@data-original-title,'Compare this Product')]")
    successMessage = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    linkProductComparison = (By.LINK_TEXT, "product comparison")
    btnListView = (By.XPATH, "//i[@class='fa fa-th-list']")


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
        self.driver.find_element(*ProductComparePage.linkProductComparison).click()

    def click_on_list_view_button(self):
        self.driver.find_element(*ProductComparePage.btnListView).click()

    def compare_this_product_option_available_on_the_product(self):
        self.driver.find_element(*ProductComparePage.compareThisProductOptionOnProduct).click()

