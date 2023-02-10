import os
import time
from time import sleep
from selenium import webdriver
from django.test import TestCase
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser
from selenium.webdriver.common.keys import Keys
from EducaPlus.tests import test_functional_base
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
        
class FunctionalTestsUsers(TestCase, StaticLiveServerTestCase):
    
    def test_users_register_page(self):
        
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        sleep(1)
        log = browser.find_element(By.ID, 'log')
        log.click()
        sleep(1)
        register = browser.find_element(By.ID, 'register')
        register.click()
        sleep(5)
        assert 'Register' in browser.title
        browser.quit()

    def test_users_login(self):

        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        sleep(5)
        assert 'Login' in browser.title
        browser.quit()

    def test_users_login_datas(self):

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
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        assert "Dashboard" in browser.title
        browser.quit()

    def test_users_register_datas(self):
       
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
        wait = WebDriverWait(browser, 10)
        log = browser.find_element(By.ID, 'log')
        log.click()
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
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(5)
        assert "Login" in browser.title
        browser.quit()

    def test_users_logout(self):

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
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(1)
        image = wait.until(EC.presence_of_element_located((By.ID, 'service')))
        image.click()
        sleep(1)
        click_logout = wait.until(EC.presence_of_element_located((By.ID, 'logout')))
        click_logout.click()
        sleep(5)
        assert "Login" in browser.title
        browser.quit()

    def test_user_perfil(self):

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
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(2)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("Sselenium2@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sel12345.")
        password.send_keys(Keys.RETURN)
        sleep(1)
        image = wait.until(EC.presence_of_element_located((By.ID, 'service')))
        image.click()
        sleep(1)
        click_perfil = wait.until(EC.presence_of_element_located((By.ID, 'profile')))
        click_perfil.click()
        sleep(1)
        assert "Detail User" in browser.title