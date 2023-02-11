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
from pathlib import Path
from selenium.webdriver.chrome.service import Service
from EducaPlus.tests.factories import *

ROOT_PATH = Path(__file__).parent.parent
CHROMEDRIVER_NAME = 'chromedriver'
CHROMEDRIVER_PATH = ROOT_PATH / 'bin' / CHROMEDRIVER_NAME

def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)
    

    chrome_service = Service(executable_path=CHROMEDRIVER_PATH)
    browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return browser

class Base_test_functional_pages(TestCase, StaticLiveServerTestCase):


    def setUp(self) -> None:
        return super().setUp

    def tearDown(self) -> None:
        return super().tearDown()


    
