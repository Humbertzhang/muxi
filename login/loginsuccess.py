import requests
from bs4 import BeautifulSoup
from time import sleep

def getjid(setcookie):
    start = setcookie.find("=") + 1
    end = setcookie.find(";")
    return setcookie[start:end]

def getltid(html):
    soup = BeautifulSoup(html, "html5lib")
    ltid = soup.find_all('input')[2]['value']
    execution = soup.find_all('input')[3]['value']
    print("ltid:" + ltid + "\nexecution:" + execution)
    return ltid, execution

def step1():
    url = "https://account.ccnu.edu.cn/cas/login"
    headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36"
    }
    r = requests.get(url, headers = headers)
    print(r.headers)
    ltid, execution =  getltid(r.text)
    jid = getjid(r.headers['set-cookie'])
    return jid, ltid, execution

def step2(jid, ltid, execution):
    url = "https://account.ccnu.edu.cn/cas/login;jsessionid=" + jid
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en,zh-CN;q=0.9,zh;q=0.8",
        'cache-control': "no-cache",
        'connection': "keep-alive",
        'content-type': "application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "Cookie":"JSESSIONID=" + jid,
        "Referer":"https://account.ccnu.edu.cn/cas/login",
        'host': "account.ccnu.edu.cn",
        'origin': "https://account.ccnu.edu.cn",
        'pragma': "no-cache",
    }
    payload = {
        "username":"---",
        "password":"---",
        "lt":ltid,
        "execution": execution,
        "_eventId":"submit",
        "submit":"LOGIN"
    } 
    r = requests.post(url, headers = headers, data = payload)
    print(r.status_code)
    print(r.text)
    print(r.headers)
if __name__ == '__main__':
    jid, ltid, execution = step1()
    step2(jid, ltid, execution)
