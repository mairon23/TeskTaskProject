import pytest
from selenium import webdriver
from data.test_data import Routes


@pytest.fixture
def driver():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(Routes.main_page)
    yield driver
    driver.quit()
