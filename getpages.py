from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as b
import time

class Getpages:
    def __init__(self,driver,username):
        self.driver = driver
        self.username = username
        
    def get_followers(self):
        bt = self.driver.find_element_by_xpath("//a[contains(@href,'/{}')]".format(self.username))
        bt.click()
        