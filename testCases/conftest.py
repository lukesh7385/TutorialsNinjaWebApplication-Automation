import os
from datetime import datetime
import allure
import pytest
import pytest_html
from pytest_html import extras
from selenium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


@pytest.fixture(scope="function")
def setup(browser):
    global driver
    if browser == "chrome":
        service = Service("C:\\Drivers\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching Chrome browser")
    elif browser == "firefox":
        service = FirefoxService("C:\\Drivers\\geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.binary_location = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        driver = webdriver.Firefox(service=service, options=options)
        print("Launching Firefox browser")
    elif browser == "edge":
        service = EdgeService("C:\\Drivers\\msedgedriver.exe")
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
        print("Launching Edge browser")
    elif browser == "headless":
        service = Service("C:\\Drivers\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # Updated headless option
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching Headless mode (Chrome)")
    else:
        service = Service("C:\\Drivers\\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(service=service, options=options)
        print("Launching Chrome browser")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver  # Return the driver instance to the test
    driver.quit()  # Ensure the browser is closed after the test


@pytest.fixture(scope="function")
def log_on_failure(request, setup):
    """
    Attaches a screenshot to the Allure report upon test failure.
    """
    driver = setup  # Access the driver instance provided by the setup fixture

    yield  # The test execution happens here

    # Check if the test case failed
    if request.node.rep_call.failed:
        # Capture a screenshot and attach it to the Allure report
        allure.attach(
            driver.get_screenshot_as_png(),
            name=f"{request.node.name}_screenshot",
            attachment_type=AttachmentType.PNG
        )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures and stores the test result for use in fixtures like log_on_failure.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
    extra = getattr(rep, "extras", [])
    if rep.when == "call":
        # Always add a URL to the report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        xfail = hasattr(rep, "wasxfail")
        if (rep.skipped and xfail) or (rep.failed and not xfail):
            # Set up the Screenshots folder
            screenshots_folder = os.path.join(os.getcwd(), "Screenshots")
            os.makedirs(screenshots_folder, exist_ok=True)

            # Generate a full file path
            file_name = f"{item.name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            file_path = os.path.join(screenshots_folder, file_name)

            # Save the screenshot using Selenium
            driver.get_screenshot_as_file(file_path)  # Replace 'driver' with your Selenium WebDriver instance

            # Attach the screenshot to an HTML report
            extra_html = '<div><img src="%s" style="width:250px;height:200px;" ' \
                         'onclick="window.open(this.src)" align="right"/></div>' % file_path
            extra.append(pytest_html.extras.html(extra_html))

        rep.extra = extra
    return rep

@pytest.fixture()
def browser(request):
    """
    Provides the browser option specified via the command-line argument.
    """
    return request.config.getoption("--browser")


def pytest_addoption(parser):
    """
    Adds a command-line option to specify the browser for testing.
    """
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(params=[
    ("adelukesh@gmail.com", "12345", "Pass"),
    ("adelukesh1@gmail.com", "12345", "Fail"),
    ("adelukesh@gmail.com", "48465", "Fail"),
    ("adelukesh24@gmail.com", "54851", "Fail"),
    ("", "", "Fail")
])
def data_for_login(request):
    return request.param


def pytest_html_report_title(report):
    """
    Customizes the HTML report title.
    """
    report.title = "TutorialsNinja Web Application - Automation HTML Reports"


def pytest_configure(config):
    """
    Adds custom metadata to the HTML report.
    """
    from pytest_metadata.plugin import metadata_key
    config.stash[metadata_key]["Project Name"] = "TutorialsNinja Web Application - Automation"
    config.stash[metadata_key]["Module Name"] = "Register, Login, Logout, Forgot Password, Search"
    config.stash[metadata_key]["Tester Name"] = "Lukesh Ade"


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """
    Removes unnecessary metadata entries from the HTML report.
    """
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)