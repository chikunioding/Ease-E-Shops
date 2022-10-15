from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_login_link="//a[text()='Login']"
    textbox_username_xpath="//input[@id='email']"
    textbox_password_xpath="//input[@id='password']"
    textbox_login_button="//button[@id='loginBtn']"
    textbox_logout_button="//a[text()='Signout ']"

    def __init__(self,driver):
        self.driver=driver

    def setloginlink(self):
        self.driver.find_element(By.XPATH,self.textbox_login_link).click()

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def setLoginbutton(self):
        self.driver.find_element(By.XPATH,self.textbox_login_button).click()

    def setLogoutbutton(self):
        self.driver.find_element(By.XPATH,self.textbox_logout_button).click()

