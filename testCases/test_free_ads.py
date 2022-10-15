import pytest
from utilities.readProperties import ReadConfig
from pageObjects.NewPostAds import Post
from pageObjects.LoginPage import Login
import time
class Test_003_post_ads:
    baseUrl=ReadConfig.getApplicationUrl()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    def test_free_ads(self,setup):
        self.driver= setup
        self.driver.get(self.baseUrl)
        self.lp=Login(self.driver)
        self.lp.setloginlink()
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.mp=Post(self.driver)
        self.mp.setpostads()
        self.driver.implicitly_wait(10)
        self.mp.setcategory()
        self.driver.implicitly_wait(10)
        self.mp.setsubcategory()
        self.driver.implicitly_wait(5)
        self.mp.setadd_type()
        self.mp.settitle()
        self.mp.setdescribe()
        self.driver.implicitly_wait(5)
        self.mp.setitemCondition()
        self.driver.implicitly_wait(10)
        self.mp.setmoney()
        self.mp.setUploadimage()
        self.mp.setsellername()
        self.mp.setsellerEmail()
        self.mp.setphone()
        self.mp.setlocation()
        self.driver.implicitly_wait(10)
        self.mp.setsub_M_location()
        self.mp.setcity()
        self.mp.setsubmitbutton()
        self.mp.setmessage()
        self.driver.close()

