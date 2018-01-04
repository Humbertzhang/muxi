#coding:utf-8
from selenium import webdriver
import time
from pprint import pprint

###GLOBALs###
browser = webdriver.Firefox()
ENOUGH_WAIT_TIME = 5
WAIT_TIME = 0.3
UID = "2016210942"
PSWD = "humbert123456781"
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
def choose_by_key():
    #想选的ID或任何其他查询条件
    idss = ["电影"]
    for ids in idss:
        browser.find_element_by_name("searchInput").send_keys(ids)
        browser.find_element_by_name("query").click()

        try:
            #第一个选课的按钮若没有则异常
            browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[21]/button').click()
        except:
            print(ids + "课程选课发生异常")
            browser.refresh()
            time.sleep(ENOUGH_WAIT_TIME)
            continue
        #点击选课 和 点击叉号 循环
        status = choose_loop()
        if status:
            print(ids + "课程选课成功")
        browser.refresh()
        time.sleep(ENOUGH_WAIT_TIME)
        browser.find_element_by_xpath('//*[@id="searchBox"]/div/div[2]/div/div/div/div/a/span')

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
    #默认选项第一项，如果为马克思之类很多课需要手动改一共有多少
    coursesNum = 15
    while True:
        i = 1
        while i < coursesNum:
            time.sleep(WAIT_TIME)
            browser.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div[2]/table/tbody/tr['+ str(i) + ']/td[21]/button').click()
            try:
                #如果没有叉号则选课成功了
                browser.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()
            except:
                return True
            i+=1

if __name__ == '__main__':
    init()
    if MOD == 1:
        choose_by_key()
    elif MOD == 2:
        choose_th()
    elif MOD == 3:
        choose_tx()
