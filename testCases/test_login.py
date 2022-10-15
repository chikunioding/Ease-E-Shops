import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_001_login:
    baseURL=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_home_page_title(self,setup):
        self.logger.info("********Test_001_login********")
        self.logger.info("*******Verifying Home Page********")
        self.driver= setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        time.sleep(5)
        self.driver.close()
        if act_title=="Lara Classified - Qspiders all in one":
            assert True
            self.logger.info("***** test title homepage passed********")
        else:
            assert False

    def test_login(self,setup):
        self.logger.info("******verifying login test title******")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setloginlink()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.setLoginbutton()
        act_headline=self.driver.title
        self.lp.setLogoutbutton()
        self.driver.close()
        if act_headline=="My account":
            assert True
            self.logger.info("***** test case login is passed*****")
        else:
            assert False

