from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WishListPage:
    wishListOption = (By.XPATH, "//div[@id='product-product']//div[@class='btn-group']//button[1]")
    wishListLink = (By.LINK_TEXT, "wish list")
    productName = (By.XPATH, "//body[1]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]")



    def __init__(self, driver):
        self.driver = driver

    def click_on_add_to_wish_list_option_displayed_in_product_display_page(self):
        wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.wishListOption)
        )
        wish_list_option.click()

    def click_on_wish_list_link_in_success_message(self):
        wish_list_link = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.wishListLink)
        )
        wish_list_link.click()

    def get_product_from_my_wish_list_page(self):
        product_name = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.productName)
        )
        return product_name.text