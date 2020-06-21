from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from bs4 import BeautifulSoup as b
import time
import login
import getpages



username='trialpiece61'
password='potato@youme'
driver=0
def main():
    global driver
    print('running script..')
    driver=webdriver.Chrome('C://Users/tikun/Desktop/Applications/chromedriver.exe')
    l=login.Login(driver,username,password)
    l.signin()
    pt = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
    pt.click()
    time.sleep(2)
    pq = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    pq.click()
    time.sleep(2)
    m = getpages.Getpages(driver,username) 
    m.get_followers()
    
if __name__ == '__main__':
    main()
    