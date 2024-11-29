import pytest
from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from utilities.read_config import Read_Config


@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config_data():
    # Load configuration data from login.ini
    return {
        "login_url_page": Read_Config.get_login_url_page(),
    }

# Get Data Testcases dari config
@pytest.fixture(params=[
    "login1",
    "login2",
    "login3",
    "login4",
    "login5"
    ])
def all_ecommerce_login(request):
    # Check Case
    return Read_Config.get_all_login_data(request.param)
















# Format html-report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'QA Practice Project'
    config.stash[metadata_key] ['Test Modul Name'] = 'Login Ecommerce Shop'
    config.stash[metadata_key] ['Tester Name'] = 'Rahmat Hidayat'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

