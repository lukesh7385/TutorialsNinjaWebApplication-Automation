from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddToCartPage:
    wishListHeaderOption = (By.CSS_SELECTOR, "a[id='wishlist-total'] span[class='hidden-xs hidden-sm hidden-md']")
    addToWishListOption = (By.XPATH, "//button[@type='button']//i[@class='fa fa-heart']")
    addToCartIconOption = (By.XPATH, "//button[@class='btn btn-primary']")
    shoppingCartHeaderOption = (By.XPATH, "(//span[normalize-space()='Shopping Cart'])[1]")
    productName = (By.XPATH, "//body[1]/div[2]/div[2]/div[1]/form[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/a[1]")
    addToCartButton = (By.XPATH, "//div[@class='button-group']//i[@class='fa fa-shopping-cart']")
    cartButtonInBlack = (By.XPATH, "//button[@type='button' and @data-toggle='dropdown']")
    viewCartOption = (By.XPATH, "//*[@id='cart']/ul/li[2]/div/p/a[1]/strong")
    macSubcategoryOption = (By.XPATH, "//a[3]")
    addToCartButtonFromFeaturedHomePage = (By.XPATH, "//span[contains(text(), 'Add to Cart')]")

    def __init__(self, driver):
        self.driver = driver

    def click_on_wish_list_header_option(self):
        wishlist_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(AddToCartPage.wishListHeaderOption)
        )
        self.driver.execute_script("arguments[0].click();", wishlist_option)

    def click_on_add_to_wish_list_from_search_result(self):
        self.driver.find_element(*AddToCartPage.addToWishListOption).click()

    def click_on_add_to_cart_icon_option_from_my_wish_list(self):
        try:
            # Wait for the "Add to Cart" icon to be clickable
            add_to_cart_icon = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable(AddToCartPage.addToCartIconOption)
            )
            add_to_cart_icon.click()
            print("Add to Cart icon clicked successfully from wishlist!")
        except Exception as e:
            print(f"Error clicking Add to Cart icon from wishlist: {e}")

    def click_on_sopping_cart_header_option(self):
       shopping_cart_header_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
           EC.presence_of_element_located(AddToCartPage.shoppingCartHeaderOption)
       )
       self.driver.execute_script("arguments[0].click();", shopping_cart_header_option)

    def get_product_name(self):
        product_name = self.driver.find_element(*AddToCartPage.productName).text
        return product_name

    def click_on_add_to_cart_button_on_product_display_in_search_result(self):
        self.driver.find_element(*AddToCartPage.addToCartButton).click()

    def click_on_cart_button_in_black_color_beside_of_search_icon(self):
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=3)
            cart_button = wait.until(EC.element_to_be_clickable(AddToCartPage.cartButtonInBlack))
            cart_button.click()
            print("Successfully clicked on the black cart button beside the search icon.")
        except Exception as e:
            print(f"Failed to click on the cart button: {e}")
            raise

    def click_on_view_cart_option(self):
        try:
            wait = WebDriverWait(self.driver, 10, poll_frequency=2)
            view_cart_option = wait.until(EC.element_to_be_clickable(AddToCartPage.viewCartOption))
            view_cart_option.click()
            print("Clicked on 'View Cart' option successfully.")
        except Exception as e:
            print(f"Failed to click on 'View Cart' option: {e}")
            raise

    def click_on_mac_subcategory_option_from_the_left_side_options(self):
        self.driver.find_element(*AddToCartPage.macSubcategoryOption).click()

    def is_title_of_the_page(self, expected_title):
        WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.title_is(expected_title)  # Wait for exact match
        )
        return self.driver.title

    def click_on_add_to_cart_button_on_featured_home_page(self):
        add_to_cart_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(AddToCartPage.addToCartButtonFromFeaturedHomePage)
        )
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)
