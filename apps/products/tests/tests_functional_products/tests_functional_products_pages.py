import os
import time
from time import sleep
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class FunctionalTestsProducts(TestCase):
    
    def test_food_list_page(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/login/')
        wait = WebDriverWait(browser, 10)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("sec1@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        alm = wait.until(EC.presence_of_element_located((By.ID, 'alimentos')))
        alm.click()
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'alimentos2')))
        alm1.click()
        sleep(5)
        assert "List Food" in browser.title
        browser.quit()