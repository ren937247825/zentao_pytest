from selenium import webdriver
from common.base import Base

host = "http://127.0.0.1:81"
url = host + "/zentao/user-login-L3plbnRhby9teS5odG1s.html"

#--------定位元素信息--------
loc1 = ("id","account")
loc2 = ("css selector","[name='password']")
loc3 = ("xpath","//*[@id='submit']")

def login(driver,user="admin",psw="123456"):
    "普通登录函数"
    zen = Base(driver)
    driver.get(url)
    zen.sendKeys(loc1,user)
    zen.sendKeys(loc2,psw)
    zen.click(loc3)

if __name__=="__main__":
    driver = webdriver.Chrome()
    login(driver)

