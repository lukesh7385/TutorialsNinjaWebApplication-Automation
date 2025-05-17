from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDisplayPage:
    thumbnailImage = (By.CLASS_NAME, "thumbnail")
    nextRightArrowButton = (By.XPATH, "/html/body/div[2]/div/button[2]")
    prevLeftArrowButton = (By.XPATH, "/html/body/div[2]/div/button[1]")
    firstThumbnailImage = (By.CSS_SELECTOR, ".mfp-img")
    secondThumbnailImage = (By.XPATH, "/html/body/div[2]/div/div[1]/div/figure/img")
    crossOption = (By.XPATH, "/html/body/div[2]/div/div[1]/div/button")


    def __init__(self, driver):
        self.driver = driver

    def click_on_thumbnail_image(self):
        self.driver.find_element(*ProductDisplayPage.thumbnailImage).click()

    def thumbnail_image_is_display(self):
        self.driver.find_element(*ProductDisplayPage.firstThumbnailImage).is_displayed()

    def click_on_next_arrow_button(self):
        try:
            next_button = WebDriverWait(self.driver, 5, poll_frequency=1).until(
                EC.element_to_be_clickable(ProductDisplayPage.nextRightArrowButton)
            )
            next_button.click()
        except Exception as e:
            print(f"Error clicking next arrow button: {e}")

    def next_arrow_button_is_display(self):
        try:
            next_button = WebDriverWait(self.driver, 5, poll_frequency=1).until(
                EC.visibility_of_element_located(ProductDisplayPage.nextRightArrowButton)
            )
            return next_button.is_displayed()
        except TimeoutException:
            return False  # Returns False if the element is not found within the timeout

    def click_on_prev_arrow_button(self):
        try:
            prev_button = WebDriverWait(self.driver, 5, poll_frequency=1).until(
                EC.element_to_be_clickable(ProductDisplayPage.prevLeftArrowButton)
            )
            prev_button.click()
        except Exception as e:
            print(f"Error clicking previous arrow button: {e}")

    def prev_arrow_button_is_display(self):
        try:
            back_button = WebDriverWait(self.driver, 5, poll_frequency=1).until(
                EC.visibility_of_element_located(ProductDisplayPage.prevLeftArrowButton)
            )
            return back_button.is_displayed()
        except TimeoutException:
            return False  # Fails gracefully if the button isn't found within the timeout

    def first_thumbnail_image_in_light_view_is_display(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(ProductDisplayPage.firstThumbnailImage)
            )
            return element.is_displayed()
        except TimeoutException:
            print("Thumbnail image not found")
            return False

    def second_thumbnail_image_in_light_view_is_display(self):
        try:
            thumbnail = WebDriverWait(self.driver, 5, poll_frequency=1).until(
                EC.visibility_of_element_located(ProductDisplayPage.secondThumbnailImage)
            )
            return thumbnail.is_displayed()
        except TimeoutException:
            return False

    def click_on_cross_option(self):
        try:
            cross_button = WebDriverWait(self.driver, 5, poll_frequency=1).until(
                EC.element_to_be_clickable(ProductDisplayPage.crossOption)
            )
            cross_button.click()
        except TimeoutException:
            print("Cross option button was not found within the timeout!")
