from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest
import json

@pytest.fixture(scope="class")
def browser(request):
    with open('./config/cfg.json') as config_file:
        data = json.load(config_file)
    if data['browser'] == 'Chrome':
        driver = webdriver.Chrome('./drivers/chromedriver.exe')
    elif data['browser'] == 'Firefox':
        driver = webdriver.Firefox('./drivers/geckodriver.exe')
    elif data['browser'] == 'Opera':
        driver = webdriver.Chrome('./drivers/operadriver.exe')
    else:
        raise Exception(f'"{data["browser"]}" is not a supported browser')
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()