#############################################################################
#sendfile.py
#author: xiaoqing sunny, date:2018-10-04
#function: upload and download the file
#############################################################################
#coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#python3 没有此模块 import SendKeys

import pyHook
from pymouse import PyMouse
from pykeyboard import PyKeyboard

driver = webdriver.Firefox()

#########################################
#上传文件 Ok
#driver.get("http://thyrsi.com//")
########################
#标签input,type=file,选择输入文件路径 ok
#driver.find_element("name","uploadimg").send_keys(r"C:\Users\a\Pictures\alphabet-tracing-worksheet-writing-z-44028488.jpg")
#driver.find_element("class name","button").click()
##################
#隐式等待   ok
#driver.implicitly_wait(10)
#driver.find_element_by_link_text("新窗口打开浏览 »").click()
#ok driver.find_element_by_xpath("//*[contains(text(),'新窗口打开浏览')]").click()
##################
#显式等待 ok
#WebDriverWait(driver,10).until(lambda x:x.find_element_by_link_text("新窗口打开浏览 »")).click()

#all_h = driver.window_handles
#print(all_h)

#driver.switch_to.window(all_h[1])
#time.sleep(3)
#关闭当前窗口
#driver.close()
#关闭所有窗口
#time.sleep(3)
#driver.quit()
###############################################

############################################
#下载文件
driver.get("https://www.criticalthinking.org/files/SAM_Aspiring_Thinkers_GuideOPT.pdf")
time.sleep(2)
driver.find_element_by_id("download").click()

#########################
#监听键盘的输入   ok
# time.sleep(3)
#默认在取消按钮,转换到保存按钮
#k = PyKeyboard()
#按下TAB,再按下ENTER
#k.press_key(k.tab_key)
#k.release_key(k.tab_key)
#time.sleep(3)
#ok k.press_key(k.enter_key)
#ok k.release_key(k.enter_key)
###########################

#########################
#TAP功能实现,内部函数其实是按下和release两个功能Ok
#k.tap_key(k.tab_key)
#time.sleep(3)
#k.tap_key(k.enter_key)
#######################

########################
#click(x,y,button,n):button1left,2right;1once,2double
#使用鼠标操作按键  ok
#time.sleep(5)
#m = PyMouse()
#x_dim,y_dim=m.screen_size()
#print(x_dim)
#print(y_dim)
#m.click(820,520,1,2)
#############################
#SendKeys.Sendkeys("TAB")
#time.sleep(2)
#SendKeys.Sendkeys("ENTER")
###########################

###########################
#选择取消,不保存下载  ok
time.sleep(5)
m = PyMouse()
x_dim,y_dim=m.screen_size()
print(x_dim)
print(y_dim)
m.click(900,520,1,1)
########################