from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest
import string
import random
import time


@pytest.mark.usefixtures('browser')
class Test_01:
    def test_homepage(self):
        self.driver.get('http://automationpractice.com/index.php')
        assert self.driver.title == 'My Store'

    def test_create_account(self):
        self.driver.find_element(By.LINK_TEXT, 'Sign in').click()
        assert self.driver.title == 'Login - My Store'
        self.driver.find_element(By.ID, 'email_create').clear()
        self.driver.find_element(By.ID, 'email_create').send_keys(''.join(random.choice(string.ascii_letters)
                                                                          for i in range(10)) + '@gmail.com')
        self.driver.find_element(By.ID, 'SubmitCreate').click()

    def test_registration_form(self):
        self.driver.find_element(By.ID, 'id_gender1').click()
        self.driver.find_element(By.ID, 'customer_firstname').send_keys('Abcdefgh')
        self.driver.find_element(By.ID, 'customer_lastname').send_keys('Ijklmnop')
        self.driver.find_element(By.ID, 'email')
        self.driver.find_element(By.ID, 'passwd').send_keys(''.join(random.choice(string.punctuation) for i in range(5)))
        self.driver.find_element(By.ID, 'id_gender1').send_keys('')
        self.driver.find_element(By.ID, 'firstname')
        self.driver.find_element(By.ID, 'lastname')
        self.driver.find_element(By.ID, 'address1').send_keys(''.join(random.choice(string.ascii_letters) for i in range(15)))
        self.driver.find_element(By.ID, 'city').send_keys('Moscow')
        self.driver.find_element(By.ID, 'id_country').send_keys('United States')
        select = Select(self.driver.find_element_by_id('id_state'))
        select.select_by_visible_text('Illinois')
        self.driver.find_element(By.ID, 'postcode').send_keys(''.join(random.choice(string.digits) for i in range(5)))
        self.driver.find_element(By.ID, 'phone_mobile').send_keys(''.join(random.choice(string.digits) for i in range(11)))
        self.driver.find_element(By.ID, 'submitAccount').click()
        assert self.driver.title == 'My account - My Store'
        print('New account was created')




