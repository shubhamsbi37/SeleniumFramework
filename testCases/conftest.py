from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        obj = Service()
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(service=obj, options=options)
    elif browser == 'edge':
        obj = Service()
        options = webdriver.EdgeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Edge(service=obj, options=options)
    elif browser == 'firefox':
        obj = Service()
        options = webdriver.FirefoxOptions()
        options.add_argument('detach')
        driver = webdriver.Firefox(service=obj, options=options)

    return driver


def pytest_addoption(parser):
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')


def pytest_configure(config):
    config.metadata['Project Name'] = 'Registeration'
    config.metadata['Module Name'] = 'Sel_register'
    config.metadata['Tester'] = 'Shubham'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html "
