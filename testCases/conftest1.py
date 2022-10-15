from selenium import webdriver
import pytest

@pytest.fixture()
def markup():
    driver=webdriver.Chrome(r"C:\Users\Mayur\PycharmProjects\Ease-E-Shops\chromedriver.exe")
    return driver
