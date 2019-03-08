#############################################################################
#element.py
#author: xiaoqing sunny, date:2018-10-14
#function: check if the element exist
#############################################################################
#coding = utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://github.com/login")
driver.implicitly_wait(10)
time.sleep(3)

#############################################################
#name: is_element_exist()
#function: check if the element exist
#result: exist--true; not--false
#method: css
#############################################################
#def is_element_exist(css):
#    s = driver.find_elements_by_css_selector(css_selector=css)
#    if len(s) == 0:
#        print("未找到元素:%s"%css)
#        return False
#    elif len(s) == 1:
#        return True
#    else:
#        print("找到%s个元素:%s"%(len(s),css))
#        return False
#if is_element_exist("#login_field"):
#    driver.find_element_by_id("login_field").send_keys("youruser")
############################################################


#############################################################
# name: is_element_exist()
# function: check if the element exist
# result: exist--true; not--false
# method: xpath
#############################################################
#def is_element_exist(path):
#    s = driver.find_elements_by_xpath(xpath=path)
#    if len(s) == 0:
#        print("未找到元素:%s"%path)
#        return False
#    elif len(s) == 1:
#        return True
#    else:
#        print("找到%s个元素:%s"%(len(s),path))
#        return False
#if is_element_exist("//*[@id='login_field']"):
#   driver.find_element_by_id("login_field").send_keys("youruser")
#############################################################

#######################
#try except:         ok
def isElementExist(css):
    try:
        driver.find_element_by_css_selector(css)
        return True
    except:
        return False
print(isElementExist("#login_field"))
#########################

##################################################
#get the attribute :tag,text,id,
#get_attribute(type,class,name,value)  ok
######################################################


driver.find_element_by_id("login_field").send_keys("youruser")
tag = driver.find_element_by_id("login_field").tag_name
print(tag)
#text = driver.find_element_by_id("login_field").text
#print(text)

type = driver.find_element_by_id("login_field").get_attribute("type")
print(type)
name = driver.find_element_by_id("login_field").get_attribute("name")
print(name)
classname = driver.find_element_by_id("login_field").get_attribute("class")
print(classname)
value = driver.find_element_by_id("login_field").get_attribute("value")
print(value)
########################
print(driver.name)  #firefox
#driver.find_element_by_id("login_field").send_keys("youruser")
#driver.find_element_by_id("password").send_keys("youruser")
#driver.find_element_by_name("commit").click()
#driver.quit()

