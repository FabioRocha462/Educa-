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
        wait = WebDriverWait(browser, 5)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("sec@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(5)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'alimentos')))
        alm.click()
        sleep(5)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'alimentos2')))
        alm1.click()
        assert "List Food" in browser.title
        sleep(1)
        browser.quit()
        
    def test_request_food_and_list_page(self):
        
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/login/')
        wait = WebDriverWait(browser, 5)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("sec1@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(5)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'alimentos')))
        alm.click()
        sleep(5)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'alimentos3')))
        alm1.click()
        ReqFood = wait.until(EC.presence_of_element_located((By.ID, 'req_food')))
        ReqFood.click()
        input = browser.find_element(By.NAME, "name")
        input.send_keys("Feijão")
        BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'btnRequest')))
        BtnRequest.click()
        assert "List Food" in browser.title
        sleep(1)
        browser.quit()