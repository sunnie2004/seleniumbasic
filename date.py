#############################################################################
#date.py
#author: xiaoqing sunny, date:2018-9-12
#function: modify the date, there are 2 ways
#############################################################################


#coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://hotels.ctrip.com/")
#if attribute = readonly,
# js = 'document.getElementById("txtCheckOut").removeAttribute("readonly")
#####################
# way 1: clear and write date
####################
driver.find_element("id","txtCheckIn").clear()       #clear it first
driver.find_element("id","txtCheckIn").send_keys("2018-12-15")   # then input

###################
# way2: js
###################
js = 'document.getElementById("txtCheckOut").value="2018-12-25"'  #js方式修改日期
driver.execute_script(js)