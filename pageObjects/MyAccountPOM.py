from selenium import webdriver
from selenium.webdriver.common.by import By


class HomePage:
    first_name_id = "firstname"
    second_name_id = "lastname"
    username_id = "username"
    password_id = "password"
    register_button_xpath = "//input[@value='Register']"

    def __init__(self, driver):
        self.driver = driver

    def firstname(self, fname):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(fname)

    def secondname(self, lname):
        self.driver.find_element(By.ID, self.second_name_id).send_keys(lname)

    def username(self, Uname):
        self.driver.find_element(By.ID, self.username_id).send_keys(Uname)

    def pwd(self,password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def button(self):
        self.driver.find_element(By.XPATH , self.register_button_xpath).click()
