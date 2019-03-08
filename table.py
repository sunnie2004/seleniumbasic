#############################################################################
#table.py
#author: xiaoqing sunny, date:2018-10-11
#function: upload and download the file
#############################################################################
#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://data.stats.gov.cn/easyquery.htm?cn=B01")
driver.maximize_window()
##########################
#function:print the single table,result: ok
###########################
#ok print(driver.find_element_by_css_selector("table#table_main>tbody>tr:nth-child(2)>td:nth-child(2)").get_attribute('textContent'))
#ok print(driver.find_element_by_css_selector("table#table_main>tbody>tr:nth-child(2)>td:nth-child(1)").text)

#ok print(driver.find_element_by_css_selector("table.table_main>tbody>tr:nth-child(2)>td:nth-child(1)").text)

#ok print(driver.find_element_by_xpath(".//*[@class='public_table table_column']/tbody/tr[2]/td[2]").get_attribute('textContent'))
#ok print(driver.find_element_by_xpath(".//*[@class='public_table table_column']/tbody/tr[2]/td[1]").text)
###########################

###############
#换行\,或者括号()处理长代码  ok
#print(driver.find_element_by_xpath(".//*[@class='public_table table_column']/tbody/tr[2]/td[2]")\
#      .get_attribute('textContent'))
##############

####################
#function:print the line,打印某一行 result:ok
####################
#i = 0
#row = driver.find_elements_by_xpath(".//*[@class='public_table table_column']/tbody/tr[2]/td")
#length = len(row)
#print(length)
#print(type(row))
#while i < length:
#    if i == 0:
#        print(row[i].text)
#        i = i+1
#    else:
#        print(row[i].get_attribute('textContent'))
#        i = i+1
##################

###################
#function:print the column,打印某一列, result:ok
###################
#j = 0
#column = driver.find_elements_by_xpath(".//*[@class='public_table table_column']/tbody/tr/td[2]")
#length = len(column)
#print(length)
#print(type(column))
#for j in column:
#    print(j.get_attribute('textContent'))
#####################

####################
#function:print the table head,打印表头某个元素和表头 result:ok
####################
#print(driver.find_element_by_css_selector("table.table_head>thead>tr>th:nth-child(2)").text)
#head = driver.find_elements_by_css_selector("table.table_head>thead>tr>th")
#print(len(head))
#for i in head:
#    print(i.text)
####################

####################
#function: hwo to operate when there is the inline scroll bar,内嵌滚动条操作, result:ok
#####################
js = 'document.getElementsByClassName("table_container_main")[0].scrollLeft = 30'
driver.execute_script(js)