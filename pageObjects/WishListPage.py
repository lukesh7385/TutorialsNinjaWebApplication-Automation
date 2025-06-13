from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class WishListPage:
    wishListOption = (By.XPATH, "//div[@id='product-product']//div[@class='btn-group']//button[1]")
    wishListLink = (By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible'] a:nth-child(3)")
    productName = (By.XPATH, "//*[@id='content']/div[1]/table/tbody/tr/td[2]/a")
    wishListOptionFromFeaturePage = (By.XPATH, "//div[@id='content']//div[1]//div[1]//div[3]//button[2]//i[1]")
    storeLogo = (By.LINK_TEXT, "Qafox.com")
    macSubcategoryOption = (By.XPATH, "//a[3]")
    addToWishListOptionFromMacSubcategoryOption = (By.XPATH, "//button[@type='button']//i[@class='fa fa-heart']")
    addToWishListOptionInSearchResultPage = (By.XPATH, "//button[@type='button']//i[@class='fa fa-heart']")

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_to_wish_list_option_displayed_in_product_display_page(self):
        wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.wishListOption)
        )
        wish_list_option.click()

    def click_on_wish_list_link_in_success_message(self):
        wish_list_link = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.wishListLink)
        )
        self.driver.execute_script("arguments[0].click();", wish_list_link)

    def is_product_name_from_my_wish_list_page(self, pro_name):
        products = self.driver.find_elements(*WishListPage.productName)
        for product_name in products:
            if product_name.text.strip() == pro_name.strip():
                print(f"Product found: {product_name.text}")
                return product_name.text
        print(f"Product '{pro_name}' not found in wishlist.")
        return None

    def click_on_add_to_wish_list_option_on_feature_page(self):
        wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.wishListOptionFromFeaturePage)
        )
        wish_list_option.click()

    def click_on_store_logo(self):
        logo = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located(WishListPage.storeLogo)
        )
        self.driver.execute_script("arguments[0].click();", logo)

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

    def click_on_add_to_wish_list_option_display_in_search_result(self):
        wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.addToWishListOptionInSearchResultPage)
        )
        wish_list_option.click()