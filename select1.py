#############################################################################
#select1.py
#author: xiaoqing sunny, date:2018-10-27
#function: select the choice by index and sequence
#############################################################################
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

s = driver.find_element_by_name("NR")
time.sleep(2)
Select(s).select_by_index(2)
time.sleep(3)

s = driver.find_element_by_id("issw1")
time.sleep(2)
Select(s).select_by_value("2")

#driver.find_element_by_name("NR").find_element_by_xpath("//option[@value='50']").send_keys(Keys.ENTER)

