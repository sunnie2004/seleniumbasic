#############################################################################
#iframe.py
#author: xiaoqing sunny, date:2018-11-1
#function: find the iframe and watch it, sometimes can not find the element because
#          there is an iframe,need to switch to it
#############################################################################

#coding=utf-8

import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://mail.163.com/")
driver.implicitly_wait(4)

driver.find_element_by_id("x-URS-iframe")
driver.switch_to.frame("x-URS-iframe")

driver.find_element_by_name("email").send_keys("sunnie")
driver.find_element_by_name("password").send_keys("12345765")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
