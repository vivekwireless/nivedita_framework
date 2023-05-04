import pytest
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager



@pytest.fixture()
def initialize_driver():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://courses.ultimateqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    yield driver
    sleep(5)
    driver.quit()


# cross browser testing

# @pytest.fixture(params=["chrome", "edge", "safari", "firefox"])
# def initialize_driver(request):
#     parameter = request.param
#
#     if parameter == "chrome":
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#
#     elif parameter == "firefox":
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     else:
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#
#     driver.get("https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.quit()
#
# # user defined browsers
# @pytest.fixture()
# def initialize_driver():
#     parameter = Config.BROWSER.lower()
#
#     if parameter == "chrome":
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#
#     elif parameter == "firefox":
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     else:
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#
#     driver.get("https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.quit()