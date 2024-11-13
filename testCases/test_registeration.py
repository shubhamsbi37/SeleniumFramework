import pytest
from selenium import webdriver
from pageObjects.MyAccountPOM import HomePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Testregist:
    baseurl = ReadConfig.geturl()
    loggenerate = LogGen.loggen()

    def test_reg(self, setup):
        self.loggenerate.info("******* test_registration started")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.loggenerate.info('** Launching browser')
        self.driver.maximize_window()

        self.hp = HomePage(self.driver)
        self.loggenerate.info('** Firstname')
        self.hp.firstname('Shubham')
        self.loggenerate.info('** lastname')
        self.hp.secondname('Sharma')
        self.hp.username('Shubham37')
        self.hp.pwd('Shubham123')
        self.hp.button()
        self.loggenerate.info("******* test_registration Finished")
