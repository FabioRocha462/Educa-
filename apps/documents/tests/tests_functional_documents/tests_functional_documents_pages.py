import os
import time
from time import sleep
from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class FunctionalTestsDocuments(TestCase, StaticLiveServerTestCase):
    def test_memorando_list_page_form_page_detail_page_and_report_page(self):
        
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        sleep(1)
        log = browser.find_element(By.ID, 'log')
        log.click()
        sleep(1)
        register = browser.find_element(By.ID, 'register')
        register.click()
        username = browser.find_element(By.NAME, "username")
        username.send_keys("TesteSelenium2")
        sleep(1)
        email = browser.find_element(By.NAME, "email")
        email.send_keys("Sselenium2@gmail.com")
        sleep(2)
        typeUser = wait.until(EC.presence_of_element_located((By.XPATH, '//select[@class="form-control select"]')))
        select = Select(typeUser)
        select.select_by_value('secretary')
        sleep(1)
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("sel12345.")
        sleep(1)
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        sleep(1)
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(2)