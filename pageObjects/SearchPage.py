import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:

    textBoxSearchField = (By.NAME, "search")
    buttonSearch = (By.XPATH, "//i[@class='fa fa-search']")

    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product):
        attempts = 3
        for attempt in range(attempts):
            try:
                search_text_box = WebDriverWait(self.driver, 10, poll_frequency=2).until(
                    EC.element_to_be_clickable(SearchPage.textBoxSearchField)
                )
                search_text_box.clear()
                search_text_box.send_keys(product)
                break  # Success! Exit loop
            except StaleElementReferenceException:
                print(f"Attempt {attempt + 1}: Element went stale, retrying...")
                time.sleep(1)

    def click_on_search_button(self):
        search_button = WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.presence_of_element_located(SearchPage.buttonSearch)
        )
        search_button.click()


