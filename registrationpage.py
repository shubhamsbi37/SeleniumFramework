from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=obj,options=options)
driver.maximize_window()
driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
driver.find_element(By.ID, "name").send_keys('Shubham')
driver.find_element(By.ID, "email").send_keys('ghfds@gmail.com')
driver.find_element(By.ID , "gender").click()

