#############################################################################
#radio.py
#author: xiaoqing sunny, date:2018-9-17
#function: radio select
#############################################################################
#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://www.baidu.com")
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()

# ok s = driver.find_element_by_id("s1_1").is_selected()
# ok  print(s)
# ok  driver.find_element_by_id("s1_1").click()
# ok  r = driver.find_element_by_id("s1_1").is_selected()
# ok  print(r)

s = driver.find_element_by_id("s1_2").is_selected()
print(s)
driver.find_element_by_id("s1_2").click()
r = driver.find_element_by_id("s1_2").is_selected()
print(r)

