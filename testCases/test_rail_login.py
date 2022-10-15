from utilities.readProperties1 import ReadConfig1
from pageObjects.TestRail import Testrail



class Test_004_rail:
    baseUrl=ReadConfig1.getApplicationUrl()
    username=ReadConfig1.getUsername()
    password=ReadConfig1.getPassword()


    def test_004_rail(self,setup):
        self.driver= setup
        self.driver.get(self.baseUrl)
        self.mp=Testrail(self.driver)
        self.mp.setuname(self.username)
        self.mp.setpname(self.password)
        self.mp.setlbutton()
        self.mp.setadmin()
        self.mp.setuserRole()
        self.mp.setadduser()
        self.mp.setname()
        self.mp.setemail()
        self.mp.setbutton()
        self.mp.setmessage()
        print("test case is passed")
        self.driver.save_screenshot(r"C:\Users\Mayur\PycharmProjects\Ease-E-Shops\Screenshots\test_rail.jpg")
        self.driver.close()


