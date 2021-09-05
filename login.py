import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
os.environ['PATH']+=r"/usr/bin/chromedriver"
operation=input('INPUT:')
driver= webdriver.Chrome()
#1 paso definiir la url
url="https://testsheepnz.github.io/BasicCalculator.html"
driver.get(url)
driver.implicitly_wait(8)
#definir los elementos
sum1=driver.find_element_by_id('number1Field')
sum2=driver.find_element_by_id('number2Field')
sum1.send_keys(Keys.NUMPAD1,Keys.NUMPAD5)
sum2.send_keys(15)
op=driver.find_element_by_xpath("//select[@name='selectOperation']/option[text()='Subtract']").click()
#try:
#    result_btn=driver.find_element_by_class_name('btn btn-primary')
#    result_btn.click()
#except:
#    print("No elements with this class name. Skipping ")
btn=driver.find_element_by_xpath("//input[@id='calculateButton']")
btn.click()
