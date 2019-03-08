##########################################################
#ddt1.py
#author: xiaoqing sunny, date:2018-9-13
#function: decorator @ddt, read the data from the excel
##########################################################
#coding = utf-8

import ddt
import unittest
import time
import xlrd
from selenium import webdriver

#####################################
#this module is used for the different input but same function ok
#testData = [{"username":"sunnie20044","password":"1357810Hxq"},{"username":"sunnie2004","password":"1357810"}]
#data is the list including lots of dict

#####################################
#read the test data from the excel table
class ExcelUtil():
####################################
#put into the list, ok
    def dict_data1(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.count = len(self.data.sheets())
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols
        self.keys = self.table.row_values(0)  #get the first row as the keys in dict
        print("总页数:%s"%self.count)
        print("行数为:%s"%self.rowNum)
        print("列数为:%s"%self.colNum)

        if self.rowNum <= 1:
            print("总行小于1")
#########################################
#return the list including dict  ok
        else:
            r = []  #列表,装结果的序列
            i = 0
            x =0
            j = 1
            for x in range((self.rowNum)-1): #遍历行的数据
                s = {}  # 字典
                values = self.table.row_values(j)    #根据行号得到行的数据
                for i in range(self.colNum):
                    s[self.keys[i]] = values[i]
                j = j + 1
                r.append(s)      #使用append添加列表元素

            return r

#########################################
filepath = "D:\\test\\test02\\goods and customes.xlsx"
sheetName = "testlogin"
data = ExcelUtil()
testData = data.dict_data1(filepath, sheetName)
print(testData)

@ddt.ddt                         #add @ddt in front of class as the decorator
class Test(unittest.TestCase):
    def setUp(self):
        print("start")
        self.driver = webdriver.Firefox()
        url = "http://forums.huaren.us/showtopic.aspx?topicid=2346447&forumpage=1"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector("div#p_e_f>span:nth-child(3)").click()
        time.sleep(3)


    def login(self, username, psw):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password3").send_keys(psw)
        self.driver.find_element_by_id("login").click()
        time.sleep(3)

    def is_login_success(self):
        try:
            text = self.driver.find_element_by_class_name("vwmy").text
            print(text)
            return True
        except:
            return False
        finally:
            self.driver.quit()

    def tearDown(self):
        print("end")
        self.driver.quit()

    @ddt.data(*testData)                  #add @ddt in front of testcase
    def test_login(self,data):
        self.login(data["username"],data["password"])
        result = self.is_login_success()
        self.assertTrue(result)

if __name__ == "_main_":
    unittest.main()

