from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
import time


class ProductDisplayPage:
    thumbnailImage = (By.CLASS_NAME, "thumbnail")
    nextRightArrowButton = (By.XPATH, "/html/body/div[2]/div/button[2]")
    prevLeftArrowButton = (By.XPATH, "/html/body/div[2]/div/button[1]")
    firstThumbnailImage = (By.CSS_SELECTOR, ".mfp-img")
    secondThumbnailImage = (By.XPATH, "/html/body/div[2]/div/div[1]/div/figure/img")
    crossOption = (By.XPATH, "/html/body/div[2]/div/div[1]/div/button")
    quantityTextBox = (By.ID, "input-quantity")
    addToCartBtn = (By.XPATH, "//button[@id='button-cart']")
    updatedQuantity = (By.CSS_SELECTOR, "input[value='3']")
    informationText = (By.XPATH, "//div[@class='alert alert-info']")

    radioButton = (By.XPATH, "//label[normalize-space()='Radio']")
    checkBox1 = (By.XPATH, "//input[@value='10']")
    checkBox2 = (By.XPATH, "//input[@value='11']")
    inputTextField = (By.ID, "input-option208")
    dropDown = (By.XPATH, "//select[@id='input-option217']")
    inptTextArea = (By.ID, "input-option209")
    uploadFile = (By.XPATH, "//button[@id='button-upload222']")
    inputDate = (By.ID, "input-option219")
    inputTime = (By.ID, "input-option221")
    inputDateAndTime = (By.ID, "input-option220")

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

    def set_product_quantity(self, quantity):
        quantity_input_box = self.driver.find_element(*ProductDisplayPage.quantityTextBox)
        quantity_input_box.clear()
        quantity_input_box.send_keys(quantity)

    def click_on_add_to_cart_button_on_product_display_page(self):
        add_to_cart_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.element_to_be_clickable(ProductDisplayPage.addToCartBtn)  # Removed unpacking
        )
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)

    def get_default_product_quantity(self):
        default_quantity = self.driver.find_element(*ProductDisplayPage.quantityTextBox)
        return default_quantity.get_attribute("value")

    def get_updated_product_quantity(self, timeout=10, poll_frequency=2):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(
            EC.visibility_of_element_located(self.updatedQuantity)
        ).get_attribute("value")

    def get_information_text(self):
        information_text = self.driver.find_element(*ProductDisplayPage.informationText).text
        return information_text

    def click_on_radio_button(self):
        element = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.visibility_of_element_located(ProductDisplayPage.radioButton)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_check_box1(self):
        self.driver.find_element(*ProductDisplayPage.checkBox1).click()

    def click_on_check_box2(self):
        self.driver.find_element(*ProductDisplayPage.checkBox2).click()

    def enter_text_to_text_field(self, text):
        text_field = self.driver.find_element(*ProductDisplayPage.inputTextField)
        text_field.clear()
        text_field.send_keys(text)

    def enter_text_to_text_area(self, text):
        self.driver.find_element(*ProductDisplayPage.inptTextArea).send_keys(text)

    def select_dropdown_option(self):
        dropdown = Select(self.driver.find_element(*ProductDisplayPage.dropDown))
        dropdown.select_by_value("4")

    def upload_file(self):
            upload_button = self.driver.find_element(*ProductDisplayPage.uploadFile)
            upload_button.click()
            time.sleep(1)
            pyautogui.write("C:\\Users\\lukesh ade\\Credence Testing 8\\Credence Testing 21 new "
                            "batch\\AutomationProject\\TutorialsNinjaWebApplication\\resources\\sample.pdf")
            pyautogui.press("enter")
            print("File uploaded successfully using PyAutoGUI.")

    def set_date(self, date):
        self.driver.find_element(*ProductDisplayPage.inputDate).send_keys(date)

    def set_time(self, t):
        self.driver.find_element(*ProductDisplayPage.inputTime).send_keys(t)

    def set_date_and_time(self, date_and_tme):
        self.driver.find_element(*ProductDisplayPage.inputDateAndTime).send_keys(date_and_tme)

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 10, poll_frequency=2).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Alert accepted successfully.")
        except Exception as e:
            print(f"Error while accepting alert: {e}")
