#############################################################################
#handlejs.py
#author: xiaoqing sunny, date:2018-10-22
#function:switch window by js method
#############################################################################
#coding=utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver =  webdriver.Firefox()
#driver.get("http://bj.ganji.com/zhaopin/")
#driver.implicitly_wait(5)
#print(driver.title)

################
#联想词定位ok
#driver.find_element_by_id("search_keyword").send_keys(u"北京")
#driver.find_element_by_id("search_keyword").click()

#search = driver.find_elements_by_css_selector("div.gj_sys_autoc_rs>ul>li")
#print(len(search))

#for i in search:
#    print(i.get_attribute('textContent'))

#if len(search) > 1:
#    search[1].click()
#    print(driver.current_url)
#    print(driver.title)
#else:
#    print("未找到")
################

################################
#js方法通过设置target在当前窗口打开新页面,适用于target = blanket, result:ok
#js = 'document.querySelectorAll("div>dl>dd>a")[0].target = "";'
#driver.execute_script(js)
#time.sleep(3)
#driver.find_element_by_link_text("海淀").click()
################################

################################
#js方法通过设置target在当前窗口打开新页面,适用于target = blanket, testing
#################################
driver.get("http://www.sohu.com/")
driver.implicitly_wait(3)
#js = 'document.querySelectorAll("div>ul>li>a,.box boxA first")[0].target = "";'
js = 'document.querySelectorAll(".box boxB,nav>div>ul>li")[0].target = "";'
driver.execute_script(js)
driver.find_element_by_link_text("体育").click()
