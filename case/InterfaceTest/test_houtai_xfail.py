from common.base import Base
import pytest

host = "http://127.0.0.1:81"
url_hou = host+"/zentao/admin.html"

#进入后台页面测试
loc_h = ("link text","后台")

#关于禅道定位
loc_about_1 = ("id","proversion")
loc_about_2 = ("id","official")
loc_about_3 = ("id","changelog")
loc_about_4 = ("id","license")
loc_about_5 = ("id","extension")


#关于禅道测试数据
test_about_data = [
    (loc_about_1,"升级专业版本"),
    (loc_about_2,"官方网站"),
    (loc_about_3,"版本历史"),
    (loc_about_4,"授权协议"),
    (loc_about_5,"插件平台")]



class TestHouTai():
    @pytest.fixture(scope="function")
    def open_houtai(self,driver):
        '''每次用例回到后台一级界面首页'''
        self.hou = Base(driver)
        driver.get(url_hou)

        #判断后台的首页是否打开了 ，打开失败就返回False
        r = self.hou.is_title("后台管理 - 禅道xxx")
        print("后台管理页面title：%s"%r)
        return r

    @pytest.mark.aboutzentao
    @pytest.mark.parametrize("loc_about_x,text",test_about_data)
    def test_aboutzentao(self,driver,open_houtai,loc_about_x,text):
        '''关于禅道-升级专业版本'''
        if not open_houtai:
            pytest.xfail("后台打开失败，标记为xfail")
        t1 = self.hou.get_text(loc_about_x)
        assert t1 == text


if __name__=="__main__":
    #pytest.main(['-v','test_houtai.py'])
    pytest.main(['-s','-m','aboutzentao','test_houtai.py'])

