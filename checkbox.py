#############################################################################
#checkbox.py
#author: xiaoqing sunny, date:2018-9-10
#function: checkbox test by three ways, including single check, multiple check,
#          and random check
#############################################################################

#coding=utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

i = 0
driver = webdriver.Firefox()
driver.get("http://www.bzhrss.gov.cn/pages/jiaoliu/wenjuan/diaocha.html?oid=116")

########################
#find the iframe  ok
#######################
driver.find_element_by_id("iframepage")
driver.switch_to.frame("iframepage")

########################
#focus elements
#######################
#driver.maximize_window()
#target =  driver.find_elements_by_css_selector("[name='radio_02']")
#driver.execute_script("arguments[0].scrollIntoView();",target)

########################
# function: windows slide down,result:ok
#########################
#driver.maximize_window()
#js = "window.scrollTo(0,document.body.scrollHeight)"
#driver.execute_script(js)     #drop down windows
#######################

#########################
# function : multiple check result: ok
#checkboxes = driver.find_elements_by_css_selector("[name='check_014']")
#print(len(checkboxes))
#for i in checkboxes:
#    print("multiple choice")
#    print(checkboxes)
#    i.click()
#########################


########################
#function : single check result: ok
#######################
checkboxes = driver.find_elements_by_css_selector("[name='check_04']")
checkboxes[0].click()

########################
#function : random check result: ok
########################

#checkboxes = driver.find_elements_by_css_selector("[name='check_014']")
#length = len(checkboxes)
#print(length)
#print(type(length))
#t = random.randint(0,length-1)
#checkboxes[t].click()
#######################