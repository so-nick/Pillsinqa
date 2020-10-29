from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math 
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("https://ticketimpulse.webcase-dev.com/admin/")


finally:


    time.sleep(4)

    browser.quit()