import os
import allure

def runcases(name="chrome",case_path=''):
    '''执行cmd命令'''
    os.system("pytest -s --browser=%s %s -q --alluredir report"%(name,case_path))

def report():
    os.system("allure generate --clean C://Users/93724/PycharmProjects/zentao_pytest/report -o "
              "C://Users/93724/PycharmProjects/zentao_pytest/report/html")

if __name__=="__main__":
    runcases(name="chrome",case_path="case")
    report()