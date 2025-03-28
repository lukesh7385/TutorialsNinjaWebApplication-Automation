from selenium import webdriver
from pytest_metadata.plugin import metadata_key
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("--disable-notifications")
        driver.implicitly_wait(10)
        driver.maximize_window()
        print("Launching chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver = webdriver.Edge()
        driver.implicitly_wait(10)
        driver.maximize_window()
        print("Launching Edge browser")
    return driver

def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(params=[
    ("adelukesh@gmail.com", "12345", "Pass"),
    ("adelukesh1@gmail.com", "12345", "Fail"),
    ("adelukesh@gmail.com", "48465", "Fail"),
    ("adelukesh24@gmail.com", "54851", "Fail")
])

def data_for_login(request):
    return request.param

# ####################### pyTest HTML Reports ###########################
def pytest_html_report_title(report):
    report.title = "TutorialsNinja Web Application HTML Report"

def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "TutorialsNinja Web Application"
    config.stash[metadata_key]["Module Name"] = "Register, Login, Logout"
    config.stash[metadata_key]["Tester Name"] = "Lukesh Ade"

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)






