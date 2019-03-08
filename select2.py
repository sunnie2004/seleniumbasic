#############################################################################
#select2.py
#author: xiaoqing sunny, date:2018-10-30
#function: select the choice by xpath way
#############################################################################
import time
from selenium import webdriver
driver = webdriver.Firefox()

driver.get("http://hotels.ctrip.com/")

driver.find_element_by_id("txtCity").clear()
driver.find_element_by_id("txtCity").send_keys("北京")   #input the city

driver.find_element_by_id("J_roomCount").click()
driver.find_element_by_xpath("//ul[@class='n_gst_num']/li[3]").click()   #input the room,selecter

s = driver.find_element_by_name("hotellevel")
time.sleep(4)
#ok   Select(s).select_by_index(1)
#Select(s).select_by_value("5")      #ok,value is a str
Select(s).select_by_visible_text("五星级/豪华")   #ok