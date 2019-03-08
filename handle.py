###########################################################
#handle.py
#author: xiaoqing sunny, date:2018-10-20
#function: switch the windows
###########################################################
#coding=utf-8
import time
from selenium import webdriver

def open():
    k=0
    driver.get("http://bj.ganji.com/")       #open the website
    driver.implicitly_wait(10)

    driver.find_element_by_link_text("北京招聘").click()
    h = driver.current_window_handle
    print("当前窗口:"+h)
    all_h = driver.window_handles
    print("所有窗口:")
    print(all_h)

    for i in all_h:
        if i != h:
            driver.switch_to.window(i)
            print("切换到新窗口名字:"+driver.title)

    driver.find_element_by_link_text("海淀").click()
    time.sleep(5)
    all_h = driver.window_handles
    print("海淀招聘所有窗口:")
    print(all_h)

    for i in all_h:
        k = k+1

    print("目前打开窗口数目:")
    print(k)

    driver.switch_to.window(all_h[k-1])
    time.sleep(5)

    driver.close()
    driver.switch_to.window(h)

if __name__ == "_main_":
    print("hello yy")
else:
    driver=webdriver.Firefox()
    open()