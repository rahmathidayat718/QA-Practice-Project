import pytest
from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from testcases.read_properties import Read_Config


@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def config_data():
    return {
        "login_url_page": Read_Config.get_login_url_page(),
    }

@pytest.fixture(
    params=Read_Config.get_login_ecommerce_data(),
    ids=lambda param: param[3] if isinstance(param, (tuple, list)) and len(param) > 3 else "unknown"
)
def data_login_ecommerce(request):
    print(f"Fixture param: {request.param}")  # Debugging
    return request.param


















# Format html-report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'QA Practice Project'
    config.stash[metadata_key] ['Test Modul Name'] = 'Login Ecommerce Shop'
    config.stash[metadata_key] ['Tester Name'] = 'Rahmat Hidayat'

