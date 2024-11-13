import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.Volunteer_SignUp import Signup


class Test_sign:
    signup_url = ReadConfig.geturl()

    def test_sign_up(self, setup):
        self.driver = setup
        self.driver.get(self.signup_url)
        self.driver.maximize_window()

        self.obj = Signup(self.driver)
        self.obj.fname('Shubham')
        self.obj.lname('Sharma')
        self.obj.phone('8360338908')
        self.obj.country('India')
        self.obj.city('Haridwar')
        self.obj.email('xyz@gmail.com')
        self.obj.radio()


