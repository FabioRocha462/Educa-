import os
import time
from time import sleep
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase

class FunctionalTestsProducts(TestCase, LiveServerTestCase):
    
    #test functional food pages
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_food_list_page(self):
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
        
    def test_food_create_page(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/login/')
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("secFD@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(2)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'alimentos')))
        alm.click()
        sleep(2)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'alimentos2')))
        alm1.click()
        sleep(2)
        FoodCreate = wait.until(EC.presence_of_element_located((By.ID, "create_food")))
        FoodCreate.click()
        sleep(2)
        name = browser.find_element(By.NAME, "name")
        name.send_keys("Arroz Branco")
        sleep(1)
        qtdd = browser.find_element(By.NAME, "quantity")
        qtdd.send_keys(4)
        sleep(1)
        date = browser.find_element(By.NAME, "validity")
        date.send_keys("01/03/2023")
        sleep(4)
        category = browser.find_element(By.NAME, "typeCategoria")
        select = Select(category)
        select.select_by_visible_text("INOMPNP")
        sleep(2)
        btnCreate = wait.until(EC.presence_of_element_located((By.ID, "btn_enviar")))
        browser.execute_script("arguments[0].click();", btnCreate)
        sleep(5)
        assert "List Food" in browser.title
        browser.quit()
        
    def test_food_detail_page(self):
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/login/')
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("secFD@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
        hbg.click()
        sleep(2)
        alm = wait.until(EC.presence_of_element_located((By.ID, 'alimentos')))
        alm.click()
        sleep(2)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'alimentos2')))
        alm1.click()
        sleep(2)
        food_detail = wait.until(EC.presence_of_element_located((By.ID, "food_detail")))
        browser.execute_script("arguments[0].click();", food_detail)
        sleep(3)
        quantity = browser.find_element(By.NAME, "quantity")
        quantity.send_keys(3)
        sleep(1)
        submit = wait.until(EC.presence_of_element_located((By.ID, 'btn-submit')))
        submit.click()
        assert "Detail Food" in browser.title
        sleep(3)
        browser.quit()
        
    #test functional cleaning pages
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    # ----------------------------------------------------------------
    
    def test_cleaning_test_page(self):
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
        alm = wait.until(EC.presence_of_element_located((By.ID, 'limpeza')))
        alm.click()
        sleep(5)
        alm1 = wait.until(EC.presence_of_element_located((By.ID, 'limpeza1')))
        alm1.click()
        assert "List cleaning" in browser.title
        sleep(1)
        browser.quit()
        
    # def test_request_food_page(self):
        
    #     browser = webdriver.Chrome()
    #     browser.get('http://127.0.0.1:8000/users/login/')
    #     wait = WebDriverWait(browser, 5)
    #     username = browser.find_element(By.NAME,"username")
    #     username.clear()
    #     username.send_keys("sec1@gmail.com")
    #     password = browser.find_element(By.NAME, "password")
    #     password.send_keys("sec12345.")
    #     password.send_keys(Keys.RETURN)
    #     hbg = wait.until(EC.presence_of_element_located((By.ID, 'hamburguer')))
    #     hbg.click()
    #     sleep(5)
    #     alm = wait.until(EC.presence_of_element_located((By.ID, 'limpeza')))
    #     alm.click()
    #     sleep(5)
    #     alm1 = wait.until(EC.presence_of_element_located((By.ID, 'limpeza2')))
    #     alm1.click()
    #     add_cleaning = wait.until(EC.presence_of_element_located((By.ID, 'add_cleaning')))
    #     add_cleaning.click()
    #     input = browser.find_element(By.NAME, "name")
    #     input.send_keys("Desinfetante")
    #     BtnRequest = wait.until(EC.presence_of_element_located((By.ID, 'btnRequest')))
    #     BtnRequest.click()