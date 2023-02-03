import os
import time
from time import sleep
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
        
class FunctionalTestsUsers(TestCase):
    
    def test_users_register_page(self):
        
        browser = webdriver.Chrome()
        browser.get('http://127.0.0.1:8000/users/register/')
        
        sleep(5)
        browser.quit()
        
        