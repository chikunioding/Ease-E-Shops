import select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Post:
    postfree_ads_link="//a[text()=' Post Free Ads']"
    select_category="//span[text()=' Select a category ']"
    select_in_category="//li[text()=' Automobiles ']"
    select_sub_category="//span[text()=' Select a sub-category ']"
    select_in_sub_category="//li[text()='Car, Motorcycle Rental']"
    add_type_private="//label[@class='radio-inline']/input"
    ad_title="//input[@id='title']"
    described_ads="//textarea[@id='description']"
    item_condition="//*[@id='conditionBloc']/div/span/span[1]/span"
    item_in_condition="//li[text()=' New ']"
    item_price="//input[@id='price']"
    upload_image="//div[@class='form-control file-caption  kv-fileinput-caption']"
    upload_image_button="//input[@id='img1']"
    seller_name="//input[@id='seller_name']"
    seller_email="//input[@id='seller_email']"
    phone_number="//input[@id='seller_phone']"
    set_location="//span[text()=' Select a location ']"
    set_in_location="//li[text()='Maharashtra']"
    set_sub_location="//span[text()=' Select a sub-location ']"
    set_sub_sub_in_location="/html/body/span/span/span[1]/input"
    set_in_sub_location="//li[text()='Akola']"
    select_city="//span[text()=' Select a city ']"
    select_in_M_city="/html/body/span/span/span[1]/input"
    select_in_city="//li[text()='Akola']"
    button_submit="//button[text()=' Submit ']"
    confirmation_message="//div[@class='alert alert-success pgray  alert-lg']"

    def __init__(self,driver):
        self.driver=driver

    def setpostads(self):
        self.driver.find_element(By.XPATH,self.postfree_ads_link).click()

    def setcategory(self):
        self.driver.find_element(By.XPATH,self.select_category).click()
        self.driver.find_element(By.XPATH,self.select_in_category).click()

    def setsubcategory(self):
        self.driver.find_element(By.XPATH,self.select_sub_category).click()
        self.driver.find_element(By.XPATH,self.select_in_sub_category).click()

    def setadd_type(self):
        self.driver.find_element(By.XPATH, self.add_type_private).click()

    def settitle(self):
        self.driver.find_element(By.XPATH,self.ad_title).send_keys("Bentley M350")

    def setdescribe(self):
        self.driver.find_element(By.XPATH,self.described_ads).send_keys("This car 54000 kms run good in condition")

    def setitemCondition(self):
        self.driver.find_element(By.XPATH,self.item_condition).click()
        self.driver.find_element(By.XPATH,self.item_in_condition).click()

    def setmoney(self):
        self.driver.find_element(By.XPATH,self.item_price).send_keys("125000")

    def setUploadimage(self):
        #self.driver.find_element(By.XPATH,self.upload_image).send_keys(r"C:\Users\Mayur\OneDrive\Pictures\Screenshots")
        self.driver.find_element(By.XPATH,self.upload_image_button).send_keys(r"C:\Users\Mayur\OneDrive\Pictures\Screenshots")

    def setsellername(self):
        self.driver.find_element(By.XPATH,self.seller_name).send_keys("Prajkta Singh")

    def setsellerEmail(self):
        self.driver.find_element(By.XPATH,self.seller_email).send_keys("probhau@gmail.com")

    def setphone(self):
        self.driver.find_element(By.XPATH,self.phone_number).send_keys("9028782145")

    def setlocation(self):
        self.driver.find_element(By.XPATH,self.set_location).click()
        self.driver.find_element(By.XPATH, self.set_in_location).click()

    def setsub_M_location(self):
        self.driver.find_element(By.XPATH,self.set_sub_location).click()
        self.driver.find_element(By.XPATH,self.set_sub_sub_in_location).send_keys("Akola")
        self.driver.find_element(By.XPATH,self.set_in_sub_location).click()

    def setcity(self):
        self.driver.find_element(By.XPATH,self.select_city).click()
        self.driver.find_element(By.XPATH,self.select_in_M_city).send_keys("Akola")
        self.driver.find_element(By.XPATH,self.select_in_city).click()

    def setsubmitbutton(self):
        self.driver.find_element(By.XPATH,self.button_submit).click()

    def setmessage(self):
        assert self.driver.find_element(By.XPATH, self.confirmation_message).is_displayed()
        print("your test case is passed")




