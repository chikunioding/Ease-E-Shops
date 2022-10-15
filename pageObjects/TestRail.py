from selenium import webdriver
from selenium.webdriver.common.by import By

class Testrail:
    user_name="//input[@id='name']"
    pass_word="//input[@id='password']"
    login_button="//button[@id='button_primary']"
    Adminis_tration="//a[text()='Administration']"
    user_roles="//a[text()='Users & Roles']"
    add_user="//*[@id='sidebar-add-users']/a[1]"
    full_name="//input[@id='name']"
    email_id="//input[@id='email']"
    adduser_button="//*[@id='accept']"
    c_message="//div[text()='Successfully added the new user and sent an invitation email.']"
    def __init__(self,driver):
        self.driver=driver

    def setuname(self,username):
        self.driver.find_element(By.XPATH,self.user_name).send_keys(username)

    def setpname(self,password):
        self.driver.find_element(By.XPATH,self.pass_word).send_keys(password)

    def setlbutton(self):
        self.driver.find_element(By.XPATH,self.login_button).click()

    def setadmin(self):
        self.driver.find_element(By.XPATH,self.Adminis_tration).click()

    def setuserRole(self):
        self.driver.find_element(By.XPATH,self.user_roles).click()

    def setadduser(self):
        self.driver.find_element(By.XPATH,self.add_user).click()

    def setname(self):
        self.driver.find_element(By.XPATH,self.full_name).send_keys("chiku")

    def setemail(self):
        self.driver.find_element(By.XPATH,self.email_id).send_keys("niodingchiku@gmail.com")

    def setbutton(self):
        self.driver.find_element(By.XPATH,self.adduser_button).click()

    def setmessage(self):
        self.driver.find_element(By.XPATH,self.c_message).is_displayed()
