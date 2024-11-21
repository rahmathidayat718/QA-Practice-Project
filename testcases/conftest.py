import pytest
from pytest_metadata.plugin import metadata_key
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    yield driver
    driver.close()

# Format html-report
def pytest_configure(config):
    config.stash[metadata_key] ['Project Name'] = 'QA Practice Project'
    config.stash[metadata_key] ['Test Modul Name'] = 'Login Ecommerce Shop'
    config.stash[metadata_key] ['Tester Name'] = 'Rahmat Hidayat'
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)

