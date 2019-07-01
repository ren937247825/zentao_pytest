from common.base import Base
import pytest
import time

host = "http://127.0.0.1:81"
url_hou = host + "/zentao/admin.html"

#进入‘后台’页面测试
loc_h = ("link text","后台")

loc_about_1 = ("id","proversion")
loc_about_2 = ("id","official")
loc_about_3 = ("id","changelog")
loc_about_4 = ("id","license")
loc_about_5 = ("id","extension")

class TestHouTai():

    @pytest.fixture(scope="function")
    def open_houtai(self,driver):
        '''每次用例回到后台一级界面首页'''
        self.hou = Base(driver)
        driver.get(url_hou)

    def test_1(self,driver,open_houtai):
        '''关于禅道-升级专业版本'''
        t1 = self.hou.get_text(loc_about_1)
        assert t1 == "升级专业版本"

    def test_2(self,driver,open_houtai):
        '''关于禅道-官方网站'''
        t1 = self.hou.get_text(loc_about_2)
        assert t1 == "官方网站"

    def test_3(self,driver,open_houtai):
        '''关于禅道-版本历史'''
        t1 = self.hou.get_text(loc_about_3)
        assert t1 == "版本历史"

    def test_4(self,driver,open_houtai):
        '''关于禅道-授权协议'''
        t1 = self.hou.get_text(loc_about_4)
        assert t1 == "授权协议"

    def test_5(self,driver,open_houtai):
        '''关于禅道-插件平台'''
        t1 = self.hou.get_text(loc_about_5)
        assert t1 == "插件平台"

if __name__=="__main__":
    pytest.main(['-s','test_after_login.py'])