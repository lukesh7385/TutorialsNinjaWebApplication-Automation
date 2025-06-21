import time

from selenium.common import TimeoutException
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
    wishListOptionFromRightColumn = (By.XPATH, "//a[@class='list-group-item'][normalize-space()='Wish List']")
    modifyYourWishListOption = (By.XPATH, "//a[normalize-space()='Modify your wish list']")
    wishListLinkFromFooterOption = (By.XPATH, "//ul[@class='list-unstyled']//a[normalize-space()='Wish List']")
    searchBreadcrumbOption = (By.LINK_TEXT, "Search")
    addToCartButtonFromWishList = (By.XPATH, "//button[@class='btn btn-primary']//i[@class='fa fa-shopping-cart']")
    accountBreadcrumbOption = (By.LINK_TEXT, "Account")
    myWishListBreadcrumbOption = (By.LINK_TEXT, "My Wish List")

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
            EC.presence_of_element_located(WishListPage.storeLogo)
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

    def click_on_add_to_wish_list_option_on_the_product_display_in_search_result(self):
        wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.addToWishListOptionInSearchResultPage)
        )
        time.sleep(1)
        wish_list_option.click()

    def click_on_wish_list_option_from_right_column(self):
        wish_list_option_from_right_column = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.wishListOptionFromRightColumn)
        )
        self.driver.execute_script("arguments[0].click();", wish_list_option_from_right_column)

    def click_on_modify_your_wish_list_option(self):
        modify_your_wish_list_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.modifyYourWishListOption)
        )
        self.driver.execute_script("arguments[0].click();", modify_your_wish_list_option)

    def click_on_wish_list_link_from_footer_option(self):
       wish_list_from_footer_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(WishListPage.wishListLinkFromFooterOption)
        )
       self.driver.execute_script("arguments[0].click();", wish_list_from_footer_option)

    def clear_wishlist_if_not_empty(self):
        try:
            wait = WebDriverWait(self.driver, 5, poll_frequency=1)
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[1]/table")))
            print("Wishlist table found.")

            while True:
                remove_buttons = self.driver.find_elements(By.XPATH, "//table//td[6]/a")
                if not remove_buttons:
                    print("No more items to remove.")
                    break

                try:
                    remove_buttons[0].click()
                    wait.until(EC.staleness_of(remove_buttons[0]))
                    print(f"Removed item. {len(remove_buttons) - 1} left...")
                except Exception as click_err:
                    print(f"Click failed: {click_err}")
                    break

            # Final confirmation
            wait.until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "div[id='content'] p"),
                    "Your wish list is empty."
                )
            )
            print("Wishlist successfully cleared.")
            return True

        except TimeoutException:
            print("No wishlist found or it might already be empty.")
            return True
        except Exception as e:
            print(f"Error while clearing wishlist: {e}")
            return False

    def click_on_search_breadcrumb_option(self):
        search_breadcrumb_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.searchBreadcrumbOption)
        )
        self.driver.execute_script("arguments[0].click();", search_breadcrumb_option)

    def click_on_add_to_cart_button_in_wish_list(self):
        add_to_cart_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.addToCartButtonFromWishList)
        )
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)

    def click_on_account_breadcrumb_option(self):
        account_breadcrumb_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(WishListPage.accountBreadcrumbOption)
        )
        self.driver.execute_script("arguments[0].click();", account_breadcrumb_option)

    def is_enable_and_is_display(self, locator):
        web_element = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(locator)
        )
        return web_element.is_displayed() and web_element.is_enabled()