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

#帮助我们定位
loc_helpwe_1 = ("id","donate")
loc_helpwe_2 = ("id","reportbug")
loc_helpwe_3 = ("id","feedback")
loc_helpwe_4 = ("id","recommend")
loc_helpwe_5 = ("id","cowinmore")

#关于禅道测试数据
test_about_data = [
    (loc_about_1,"升级专业版本"),
    (loc_about_2,"官方网站"),
    (loc_about_3,"版本历史"),
    (loc_about_4,"授权协议"),
    (loc_about_5,"插件平台")]

#帮助我们测试数据
test_helpwe_data = [
    (loc_helpwe_1,"捐助我们"),
    (loc_helpwe_2,"汇报Bug"),
    (loc_helpwe_3,"反馈需求"),
    (loc_helpwe_4,"推荐给朋友"),
    (loc_helpwe_5,"更多方式...")
]

class TestHouTai():
    @pytest.fixture(scope="function")
    def open_houtai(self,driver):
        '''每次用例回到后台一级界面首页'''
        self.hou = Base(driver)
        driver.get(url_hou)


    @pytest.mark.aboutzentao
    @pytest.mark.parametrize("loc_about_x,text",test_about_data)
    def test_aboutzentao(self,driver,open_houtai,loc_about_x,text):
        '''关于禅道-升级专业版本'''
        t1 = self.hou.get_text(loc_about_x)
        assert t1 == text

    @pytest.mark.helpwe
    @pytest.mark.parametrize("loc_helpwe_x,text",test_helpwe_data)
    def test_helpwe(self,driver,open_houtai,loc_helpwe_x,text):
        '''帮助我们-用例'''
        t1 = self.hou.get_text(loc_helpwe_x)
        assert t1 == text

if __name__=="__main__":
    #pytest.main(['-v','test_houtai.py'])
    pytest.main(['-s','-m','aboutzentao','test_houtai.py'])

