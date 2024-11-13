import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir) + '\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def geturl():
        url = (config.get('commonInfo', 'url'))
        return url

    @staticmethod
    def first_name():
        f_name = (config.get('commonInfo', 'first_name'))
        return f_name

    @staticmethod
    def second_name():
        l_name = (config.get('commonInfo', 'last_name'))
        return l_name
