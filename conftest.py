import pytest
from selenium  import webdriver
from pages.loginpage import login

def pytest_addoption(parser):
    '''添加命令行参数--browser'''
    parser.addoption(
        "--browser",action="store",
        default="chrome",help="browser option:firefox or chrome"
    )

    #添加host参数，设置默认测试环境地址
    parser.addoption(
        "--host",action="store",
        default="http://192.168.56.1:81",help="test host->://192.168.x.xx:80"
    )

@pytest.fixture(scope="session")
def driver(request):

    name = request.config.getoption("--browser")
    if name == "firefox":
        driver = webdriver.Firefox()
    elif name == "chrome":
        driver = webdriver.Chrome()
    else:
        driver =webdriver.Chrome()
    print("正在启动浏览器名称：%s"%name)

    #先调用login函数先登录
    login(driver)

    def fn():
        print("当全部用例执行完之后：teardown driver！")
        driver.quit()

    request.addfinalizer(fn)  #终结函数
    return driver
