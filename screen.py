#############################################################################
#screen.py
#author: xiaoqing sunny, date:2018-9-21
#function: get the element including the same part by page-source
#############################################################################
#coding = utf-8

import time
from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.get("http://bj.ganji.com/")
page = driver.page_source
######findall(正则表达式,字符串,匹配任意字符号)
url_list = re.findall('href=\"(.*?)"',page,re.S)
url_all = []

for url in url_list:
    if "http" in url:
        print(url)
        url_all.append(url)
print(url_all)

