import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    continueShoppingBTN = (By.LINK_TEXT, "Continue Shopping")
    pcZeroOption = (By.XPATH, "//a[normalize-space()='PC (0)']")
    heroImages = (By.XPATH, "//div[contains(@class, 'swiper-slide-active')]//img[contains(@class, 'img-responsive')]")
    prevButton = (By.XPATH, "//*[@id='content']/div[1]/div[3]/div[2]")
    backButton = (By.XPATH, "//*[@id='content']/div[1]/div[3]/div[1]")
    swipingPropagationBulletButton = (By.XPATH,
                                      "//div[@class='swiper-pagination slideshow0 swiper-pagination-clickable swiper-pagination-bullets']//span[@class='swiper-pagination-bullet']")
    image_xpath = (By.XPATH, "//body/div[@id='common-home']/div[@class='row']/div[@id='content']/div[1]")
    fourFeaturedProducts = (By.XPATH, "//div[@class='product-layout col-lg-3 col-md-3 col-sm-6 col-xs-12']/div/div[2]/h4/a")
    macbookProductAddToCartOption = (By.XPATH, "(//span[contains(text(),'Add to Cart')])[1]")
    iPhoneProductAddToCartOption = (By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[3]/button[1]/span")
    appleCinema30ProductAddToCartOption = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/button[1]/span[1]")
    canonEOS5DProductAddToCartOption = (By.XPATH, "//*[@id='content']/div[2]/div[4]/div/div[3]/button[1]/span")
    wishlistButton1 = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[3]/button[2]")
    wishlistButton2 = (By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[3]/button[2]")
    wishlistButton3 = (By.XPATH, "//*[@id='content']/div[2]/div[3]/div/div[3]/button[2]")
    wishlistButton4 = (By.XPATH, "//*[@id='content']/div[2]/div[4]/div/div[3]/button[2]")




    def __init__(self, driver):
        self.driver = driver

    def click_on_continue_shopping_button(self):
        continue_shopping_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(HomePage.continueShoppingBTN)
        )
        continue_shopping_button.click()

    def pc_zero_product_option(self):
        zero_product_option = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(HomePage.pcZeroOption)
        )
        zero_product_option.click()

    def is_any_active_hero_image_visible(self):
        """
        Checks if any hero image in the active swiper slide is visible.

        Returns:
            True if at least one image is visible, False otherwise.
        """
        try:
            images = self.driver.find_elements(*HomePage.heroImages)
            return any(img.is_displayed() for img in images)
        except NoSuchElementException:
            return False

    def are_hero_images_auto_sliding(self, locator, cycles=3, interval=5):
        """
        Detects if any of the hero images are auto-sliding by checking for changes in 'src' over multiple cycles.

        Args:
            locator: Tuple locator for the hero image elements (e.g., HomePage.heroImages)
            cycles: Number of checks to perform (default: 3)
            interval: Time between each check in seconds (default: 5)

        Returns:
            True if any image changes during the cycle, False otherwise.
        """
        try:
            image_src_history = []

            for _ in range(cycles):
                images = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located(locator)
                )
                current_srcs = tuple(img.get_attribute("alt") for img in images)
                image_src_history.append(current_srcs)
                time.sleep(interval)

            # Check if any image src changes across cycles
            return len(set(image_src_history)) > 1

        except NoSuchElementException:
            return False

    def click_on_prev_arrow_button_on_the_hero_image(self):
        prev = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(HomePage.prevButton)
        )
        prev.click()

    def click_on_back_arrow_button_on_the_hero_image(self):
        back = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(HomePage.backButton)
        )
        back.click()

    def click_on_swiper_pagination_bullet_button(self):
        bullet_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(HomePage.swipingPropagationBulletButton)
        )
        bullet_button.click()
        bullet_button.click()

    def hover_on_swiper_pagination_bullet_button(self):
        act = ActionChains(self.driver)
        swiper_bullet_button = self.driver.find_element(*HomePage.swipingPropagationBulletButton)
        act.move_to_element(swiper_bullet_button).perform()

    def drag_swiper_image(self, offset_x=200):
        """
        Simulates a click-hold-drag action on a Swiper image to scroll horizontally.

        Args:
            offset_x (int): Horizontal drag offset in pixels. Negative = left, positive = right.

        Returns:
            bool: True if drag was successful, False otherwise.
        """
        try:
            print(f"Waiting for image element at: {HomePage.image_xpath}")
            image = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.presence_of_element_located(HomePage.image_xpath)
            )
            actions = ActionChains(self.driver)
            actions.click_and_hold(image).move_by_offset(offset_x, 0).release().perform()
            print(f"✅ Successfully dragged image by {offset_x}px")
            return True
        except Exception as e:
            print(f"❌ Error dragging image: {e}")
            return False

    def is_four_featured_product_display(self):
        featured_elements = self.driver.find_elements(*HomePage.fourFeaturedProducts)
        expected_products = ["MacBook", "iPhone", 'Apple Cinema 30"', "Canon EOS 5D"]
        actual_products = [element.text.strip() for element in featured_elements]

        missing = [product for product in expected_products if product not in actual_products]
        if missing:
            print(f"Missing featured products: {missing}")
            return False
        return True

    def click_on_macbook_add_to_cart_button(self):
        try:
            button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.presence_of_element_located(HomePage.macbookProductAddToCartOption)
            )
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", button)
            print("Clicked 'Add to Cart' for MacBook")
        except Exception as e:
            print(f"Failed to click MacBook Add to Cart button: {e}")

    def click_on_iphone_add_to_cart_button(self):
        try:
            button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.presence_of_element_located(HomePage.iPhoneProductAddToCartOption)
            )
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", button)
            print("Clicked 'Add to Cart' for iPhone")
        except Exception as e:
            print(f"Failed to click iPhone Add to Cart button: {e}")

    def click_on_apple_cinema_30_add_to_cart_button(self):
        try:
            button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.presence_of_element_located(HomePage.appleCinema30ProductAddToCartOption)
            )
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", button)
            print("Clicked 'Add to Cart' for Apple Cinema 30")
        except Exception as e:
            print(f"Failed to click Apple Cinema 30 Add to Cart button: {e}")


    def click_on_canon_eos_5d_add_to_cart_button(self):
        try:
            button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.element_to_be_clickable(HomePage.canonEOS5DProductAddToCartOption)
            )
            time.sleep(2)
            self.driver.execute_script("arguments[0].click();", button)
            print("Clicked 'Add to Cart' for Canon EOS 5D")
        except Exception as e:
            print(f"Failed to click Canon EOS 5D Add to Cart button: {e}")

    def click_on_add_to_wish_list_for_macbook(self):
        wish_list_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(HomePage.wishlistButton1)
        )
        wish_list_button.click()

    def click_on_add_to_wish_list_for_iphone(self):
        wish_list_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(HomePage.wishlistButton2)
        )
        wish_list_button.click()

    def click_on_add_to_wish_list_for_apple_cinema_30(self):
        wish_list_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(HomePage.wishlistButton3)
        )
        wish_list_button.click()

    def click_on_add_to_wish_list_for_canon_eos_5d(self):
        wish_list_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(HomePage.wishlistButton4)
        )
        wish_list_button.click()

