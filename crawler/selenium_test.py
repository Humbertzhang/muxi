#coding:utf-8

from selenium import webdriver
import time
from pprint import pprint

#login
browser = webdriver.Chrome()
browser.get("https://account.ccnu.edu.cn/cas/login?service=http%3A%2F%2Fxk.ccnu.edu.cn%2Fssoserver%2Flogin%3Fywxt%3Djw%26url%3Dxtgl%2Findex_initMenu.html")
browser.find_element_by_name("username").send_keys("2016210942")
browser.find_element_by_name("password").send_keys("humbert123456781")
time.sleep(1)
browser.find_element_by_class_name("btn-submit").click()
time.sleep(1)
#endlogin

#clike xuanke
#browser.find_element_by_class_name("col-md-4 col-sm-4 col-xs-6")
#time.sleep(2)
