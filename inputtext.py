#############################################################################
#inputtext.py
#author: xiaoqing sunny, date:2018-9-6
#function: find the element and input the text
#############################################################################
#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest

#driver =  webdriver.Firefox()
#driver.get("http://forums.huaren.us/showtopic.aspx?topicid=2346447&forumpage=1")
#####################
#放大和滑动滚动条   ok
#driver.maximize_window()
#js = "window.scrollTo(0,document.body.scrollHeight)"
#driver.execute_script(js)
####################

####################
#定位form里的图片img ok
#driver.find_element_by_xpath("//div[@id='p_e_f']/span[@class='replybtn']/a/img[@alt='回复该主题']").click()
#ok driver.find_element_by_css_selector("div#p_e_f>span:nth-child(3)").click()
#time.sleep(2) #very important timesleep

#####################
#元素定位有问题首先测试窗口ok,然后查看iframe
#all_h = driver.window_handles
#print(all_h)
######################

##################
#页面TITLE检查   Ok
#title = EC.title_is("求祝福")
#print(title(driver))
#title1 = EC.title_contains("求祝福")
#print(title1(driver))
#print(driver.title)
########################

#######################
#输入框判断弹出框是否为alert  ok
#result = EC.alert_is_present()(driver)
#if result:
#    print(result.text)
#else:
#    print("没有alert框")
########################

###################
#登陆系统  ok
#easyway ok driver.find_element_by_id("username").send_keys("sunnie20044")
##显示等待 WebDriverWait(driver.timeout,frequency)
#until(lamba x:x.find_element_by_id("")).  ok
#WebDriverWait(driver,10).until(lambda  x:x.find_element_by_id("username")).send_keys("sunnie20044")
#driver.find_element("css selector","form#form1>div>div.lgfm>div>input#username").send_keys("sunnie20044")
#driver.find_element("css selector","form#form1>div>div.lgfm>div>input#password3").send_keys("1357810Hxq")
######################
#判断文本  ok
#locator = ("id","returnmessage")
#text = "用户登录"
#result = EC.text_to_be_present_in_element(locator,text)(driver)
#print(result)
#####################
# driver.find_element_by_id("login").click()
######################

##########################
#登陆是否成功判断 ok
#driver.implicitly_wait(10)
#str = driver.find_element_by_id("returnmessage").get_attribute("class")
#if str == "onerror":
#    print("登陆不成功")
#else:
#    print("登陆成功")
#driver.find_element_by_id("username").clear()
#driver.find_element_by_id("password3").clear()
############################

#######################
#提示登陆框判断弹出框是否为alert  testing
#is_disappeared  = WebDriverWait(driver,10,1).\
#    until_not(lambda x:x.find_element_by_id("returnmessage"))
#print(is_disappeared)

#if is_disappeared:
#    print("仍在登陆")
#else:
#    result1 = EC.alert_is_present()(driver)
#    if result1:
#       print(result1.text)
#        result1.accept()
#    else:
#        print("没有alert框")
#WebDriverWait(driver,5).\
 #   until(lambda x:x.find_element_by_link_text("如果长时间没有响应请点击此处"))
#driver.get_screenshot_as_file('d:/test/test02/alert.png')

#result = EC.alert_is_present()(driver)

#if result:
#   print(result.text)
#else:
 #   print("未弹出")
########################


############################
#打开回复帖子,输入文本ok
#WebDriverWait(driver,10,1).until(lambda  x:x.find_element_by_xpath("//div[@id='p_e_f']/span[@class='replybtn']/a/img[@alt='回复该主题']")).click()
#driver.implicitly_wait(10)
#driver.find_element("id","message").send_keys("bless")
##############################

#####################
#快捷方式框输入文本  ok
#隐式等待driver.implicitly_wait(10)
#ok driver.find_element_by_id("quickpostmessage").send_keys("bless")
#driver.find_element("id","quickpostmessage").send_keys("bless")
#driver.find_element_by_id("quickpostsubmit").click()
###########################

#######################
#封装登陆方法   OK
class Blog(unittest.TestCase):
  def SetUp(self):
      self.driver = webdriver.Firefox()
      url = "http://forums.huaren.us/showtopic.aspx?topicid=2346447&forumpage=1"
      self.driver.get(url)
      self.driver.implicitly_wait(10)
      self.driver.find_element_by_css_selector("div#p_e_f>span:nth-child(3)").click()
      time.sleep(3)
  def login(self,username,psw):
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
#  def teardown(self):
#      self.driver.quit()
###########################
#错误密码
  def test03(self):
      self.SetUp()
      self.login("sunnie20044", "1357810HXQ")
      result = self.is_login_success()
      self.assertTrue(result)
##########################
#正确输入
  def test01(self):
      self.SetUp()
      self.login("sunnie20044","1357810Hxq")
      result = self.is_login_success()
      self.assertTrue(result)
      ######ok assertequal()
      #text = self.driver.find_element_by_class_name("vwmy").text
      #print(text)
      #print(self.assertEqual(text,"sunnie2004"))
#      self.teardown()
#########################
#错误帐户
  def test02(self):
      self.SetUp()
      self.login("sunnie2004","1357810Hxq")
      result = self.is_login_success()
      self.assertTrue(result)

if __name__ == "_main_":
    unittest.main()
