from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
os.environ['PATH']+=r"/usr/bin/chromedriver"
driver = webdriver.Chrome()
driver.get('https://radios.com.bo/')
driver.implicitly_wait(30)
my_element = driver.find_element_by_id('radio-button')
my_element.click()
#progress_element=driver.find_element_by_class_name("stop")
#print(f"{progress_element.alt=='Parar'}")
#WebDriverWait(driver,30).until(
#EC.text_to_be_present_in_element(
#(By.CLASS_NAME,'progress-label'),#Elements filtration
#'Complete!'#The expected text
#))
