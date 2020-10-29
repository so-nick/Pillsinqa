from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import math 
import time
import os
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    

    a = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    
    
    browser.find_element_by_id('book').click()   
   

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    xl = browser.find_element_by_id('input_value')
    x = xl.text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_tag_name('button[type="submit"]').click()

finally:


    time.sleep(5)

    browser.quit()