import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


@pytest.mark.usefixtures("setup", "log_on_failure")
@allure.severity(allure.severity_level.BLOCKER)
class Test_002_Login_Functionality:
    baseURL = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):
        self.logger.info("************************** Test_Login_001 is Start ****************************")
        self.logger.info("***************** Verifying Home Page Title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        WebDriverWait(self.driver, 10, poll_frequency=2).until(
            EC.title_is("Your Store")
        )
        self.logger.info("************************** Verifying Test_Login_001 ****************************")
        if self.driver.title == "Your Store":
            assert True
            self.logger.info("************** Home page title test is passed ************")
        else:
            self.logger.error("************** Home page title test is failed ************")
            assert False
        self.logger.info("************************** End Of Test_Login_001 ****************************")


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_functionality_001(self, setup):
        self.logger.info("************** Login test is started ************")
        self.driver = setup
        self.logger.info("navigating to the url")
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.logger.info("clicking on myAccount drop menu")
        self.lp.click_on_my_account()
        self.logger.info("clicking on login link")
        self.lp.click_on_login_link()
        self.logger.info("passing the username")
        self.lp.set_username(self.username)
        self.logger.info("passing the password")
        self.lp.set_password(self.password)
        self.logger.info("clicking on the login button")
        self.lp.click_on_login_button()

        # Wait for the title to be updated
        try:
            WebDriverWait(self.driver, 10, poll_frequency=2).until(
                EC.title_is("My Account")
            )
            act_title = self.driver.title
            self.logger.info("************** Verifying Login test ************")
            if act_title == "My Account":
                assert True
                self.logger.info("************** Login test is passed ************")
            else:
                raise AssertionError("Page title does not match!")
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\test_login_functionality_001_failed.png")
            self.logger.error("************** Login test is failed ************")
            self.logger.error(f"Error: {str(e)}")
            assert False
        finally:
            self.driver.quit()
