from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import pytest
import string
import random
import time


@pytest.mark.usefixtures('browser')
class Test_02:
    def test_homepage(self):
        self.driver.get('http://automationpractice.com/index.php')
        assert self.driver.title == 'My Store'

    def test_search(self):
        women = self.driver.find_element(By.XPATH, '//div[@id="block_top_menu"]/ul/li[1]/a')
        ActionChains(self.driver).move_to_element(women).perform()
        self.driver.find_element(By.LINK_TEXT, 'T-shirts').click()
        assert self.driver.title == 'T-shirts - My Store'
        tshirt_name = self.driver.find_element(By.XPATH, '//div[@class="product-container"]/div[@class="right-block"]'
                                                         '/h5/a[@class="product-name"]')
        self.driver.find_element(By.XPATH, "//input[@id='search_query_top']").send_keys(tshirt_name.text)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-default button-search']").click()
        assert self.driver.find_element(By.XPATH, '//div[@class="product-container"]/div[@class="right-block"]'
                                                         '/h5/a[@class="product-name"]').text == 'Faded Short Sleeve T-shirts'