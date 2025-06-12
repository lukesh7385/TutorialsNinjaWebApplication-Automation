from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WishListPage:
    wishListOption = (By.XPATH, "//div[@id='product-product']//div[@class='btn-group']//button[1]")
    wishListLink = (By.XPATH, "/html/body/div[2]/div[1]/a[2]")
    productName = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]")
    wishListOptionFromFeaturePage = (By.XPATH, "//div[@id='content']//div[1]//div[1]//div[3]//button[2]//i[1]")
    storeLogo = (By.LINK_TEXT, "Qafox.com")
    macSubcategoryOption = (By.XPATH, "//a[3]")
    addToWishListOptionFromMacSubcategoryOption = (By.XPATH, "//button[@type='button']//i[@class='fa fa-heart']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_to_wish_list_option_displayed_in_product_display_page(self):
        wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.wishListOption)
        )
        wish_list_option.click()

    def click_on_wish_list_link_in_success_message(self):
        wish_list_link = WebDriverWait(self.driver, 20, poll_frequency=4).until(
            EC.element_to_be_clickable(WishListPage.wishListLink)
        )
        wish_list_link.click()

    def get_product_name_from_my_wish_list_page(self):
        product_name = WebDriverWait(self.driver, 20, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.productName)
        )
        return product_name.text

    def click_on_add_to_wish_list_option_on_feature_page(self):
        wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.wishListOptionFromFeaturePage)
        )
        wish_list_option.click()

    def click_on_store_logo(self):
        logo = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.storeLogo)
        )
        logo.click()

    def click_on_mac_subcategory_option(self):
        mac_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.macSubcategoryOption)
        )
        mac_option.click()

    def click_on_add_to_wish_list_option_from_mac_subcategory_option(self):
        mac_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.addToWishListOptionFromMacSubcategoryOption)
        )
        mac_option.click()