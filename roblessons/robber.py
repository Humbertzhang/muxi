#coding:utf-8
from selenium import webdriver
import time
from pprint import pprint

###GLOBALs###
browser = webdriver.Firefox()
ENOUGH_WAIT_TIME = 5
WAIT_TIME = 1
UID = "X"
PSWD = "X"
# MOD = 1 为按课程号选课 MOD = 2 为选通核 MOD = 3 为选通选
MOD = 1

def init():
    browser.get("https://account.ccnu.edu.cn/cas/login?service=http%3A%2F%2Fxk.ccnu.edu.cn%2Fssoserver%2Flogin%3Fywxt%3Djw%26url%3Dxtgl%2Findex_initMenu.html")
    browser.find_element_by_name("username").send_keys(UID)
    browser.find_element_by_name("password").send_keys(PSWD)
    browser.find_element_by_class_name("btn-submit").click()
    #如果不停留，则会因为没加载出来而报错
    time.sleep(ENOUGH_WAIT_TIME)
    browser.get("http://xk.ccnu.edu.cn//xsxk/zzxkyzb_cxZzxkYzbIndex.html?gnmkdm=N253512&layout=default&su=" + UID)
    time.sleep(ENOUGH_WAIT_TIME)

#按课程号选课
def choose_by_id():
    #想选的ID
    ids = "40152005"
    browser.find_element_by_xpath('//*[@id="searchBox"]/div/div[2]/div/div/div/div/a/span').click()
    browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/input').send_keys(ids)
    choose_loop()

#通核
def choose_th():
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[6]/div/div[2]/a").click()
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[6]/div/div[1]/ul/li[9]/a").click()
    choose_loop()

#通选
def choose_tx():
    browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[3]/div[6]/div/div[1]/ul/li[6]/a")
    choose_loop()

def choose_loop():
    while True:
        time.sleep(WAIT_TIME)
        #查询
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div/span/button[1]").click()
        #点击选课后判断是否选到了
        browser.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div[2]/table/tbody/tr/td[21]/button").click()
        #选到了之后print一条信息之后，关闭对话框，继续再抢
        #没选到就直接关闭对话框
        try:
            browser.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()
        except:
            print("选到了")

if __name__ == '__main__':
    init()
    if MOD == 1:
        choose_by_id()
    elif MOD == 2:
        choose_th()
    elif MOD == 3:
        choose_tx()
