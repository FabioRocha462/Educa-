import os
import time
from time import sleep
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser
        
class FunctionalTestsUsers(TestCase, StaticLiveServerTestCase):
    
    def test_users_register_page(self):
        
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/register/')
        sleep(5)
        assert 'Register' in browser.title
        browser.quit()

    def test_users_login(self):

        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/login/')
        sleep(5)
        assert 'Login' in browser.title
        browser.quit()

    def test_users_login_datas(self):

        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("sec1@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        sleep(20)
        assert "Dashboard" in browser.title
        browser.quit()

    def test_users_register_datas(self):

        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        log = browser.find_element(By.ID, 'log')
        log.click()
        register = browser.find_element(By.ID, 'register')
        register.click()
        username = browser.find_element(By.NAME, "username")
        username.send_keys("TesteSelenium2")
        email = browser.find_element(By.NAME, "email")
        email.send_keys("Sselenium2@gmail.com")
        password1 = browser.find_element(By.NAME, "password1")
        password1.send_keys("sel12345.")
        password2 = browser.find_element(By.NAME, "password2")
        password2.send_keys("sel12345.")
        password2.send_keys(Keys.RETURN)
        sleep(5)
        assert "Login" in browser.title
        browser.quit()

    def test_users_logout(self):

        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/login/')
        wait = WebDriverWait(browser, 10)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("sec@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        image = wait.until(EC.presence_of_element_located((By.ID, 'service')))
        image.click()
        click_logout = wait.until(EC.presence_of_element_located((By.ID, 'logout')))
        click_logout.click()
        sleep(5)
        assert "Login" in browser.title
        browser.quit()

    def test_user_perfil(self):

        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/login/')
        wait = WebDriverWait(browser, 10)
        username = browser.find_element(By.NAME,"username")
        username.clear()
        username.send_keys("sec@gmail.com")
        password = browser.find_element(By.NAME, "password")
        password.send_keys("sec12345.")
        password.send_keys(Keys.RETURN)
        image = wait.until(EC.presence_of_element_located((By.ID, 'service')))
        image.click()
        click_perfil = wait.until(EC.presence_of_element_located((By.ID, 'profile')))
        click_perfil.click()
        assert "Detail User" in browser.title


        
        