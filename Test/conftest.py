import threading
import pytest as pytest
from selenium import webdriver

def open_browser(url, driver):
    driver.get(url)
    # input("enter some text")
    # driver.quit()

@pytest.fixture(scope="class")
def setup(request):
    url = "https://www.itv.com/"
    num_browsers = 5
    drivers = []

    for i in range(num_browsers):
        driver = webdriver.Chrome()
        thread = threading.Thread(target=open_browser, args=(url, driver))
        thread.start()
        drivers.append(driver)
    request.cls.drivers = drivers
    yield
    for driver in drivers:
        driver.quit()

def pytest_addoption(parser):
    parser.addoption("--web_name", type=str, help="web name")
    parser.addoption("--season_number", type=str, help="Season number")
    parser.addoption("--episode_title", type=str, help="Episode title")


@pytest.fixture(scope="function")
def web_name(request):
    return request.config.getoption("--web_name")

@pytest.fixture(scope="function")
def season_number(request):
    return request.config.getoption("--season_number")

@pytest.fixture(scope="function")
def episode_title(request):
    return request.config.getoption("--episode_title")




