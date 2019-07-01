import pytest,time

def test_01(driver):
    '''用例11-打开首页'''
    driver.get('https://www.cnblogs.com/yoyoketang/')

    time.sleep(1)
    t = driver.title

    print(t)
    assert "上海-悠悠" in t

def test_02(driver):
    '''用例2-标签页'''
    driver.get("https://www.cnblogs.com/yoyoketang/tag/pytest/")
    time.sleep(1)

    t = driver.title
    print(t)

    assert "pytest - 标签" in t

if __name__=="__main__":
    pytest.main(['-s',"--browser=chrome",'test_yoyo_blogs.py'])