import pytest
from selenium import webdriver
from common.base import Base


#-------测试数据-------
test_login_data = [('admin','123456','admin'),('admin111','11111','')]

#-------定位元素-------
loc1 = ('id','account')
loc2 = ('css selector','[name="password"]')
loc3 = ("xpath","//*[@id='submit']")

login_user = ("css selector","#userMenu>a")  #登录后的用户名

driver = webdriver.Chrome()
zen = Base(driver)
url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby9teS5odG1s.html"

def setup_function():
    driver.get(url)

def teardown_function():
    '''数据清理'''
    try:
        print("清空cookies，退出登录状态")
        driver.delete_all_cookies()
        driver.refresh()
    except:
        print("元素找不到")

def teardown_module():
    '''用例执行完成，最后退出'''
    print("teardown_class:用例执行完成，退出浏览器")
    driver.quit()

def login(user='admin',psw='123456'):
    '''普通登录函数'''
    zen.sendKeys(loc1,user)
    zen.sendKeys(loc2,psw)
    zen.click(loc3)

@pytest.mark.parametrize("user,psw,expect",test_login_data)
def test_login(user,psw,expect):
    '''登录用例'''
    login(user,psw)
    result = zen.get_text(login_user)
    print("登录结果，获取到用户名：%s"%result)
    assert result == expect

if __name__=="__main__":
    pytest.main(['-s','test_params.py'])
