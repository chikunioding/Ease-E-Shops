
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities import XLUtils
import time

class Test_002_login:
    baseURL=ReadConfig.getApplicationUrl()
    path=r"C:\Users\Mayur\Desktop\LoginData.xlsx"

    def test_login(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)

        self.rows=XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel",self.rows)

        for r in range(2, self.rows+1):
            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)

            self.lp.setloginlink()
            self.lp.setUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.setLoginbutton()
            self.driver.close()
            time.sleep(4)

            act_title=self.driver.title
            exp_title="Lara Classified - Qspiders all in one"

            assert act_title==exp_title
            print("test case is passed")




