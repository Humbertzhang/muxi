import requests
from bs4 import BeautifulSoup
from time import sleep

def getjid(setcookie):
    start = setcookie.find("=") + 1
    end = setcookie.find(";")
    return setcookie[start:end]

def getltid(html):
    soup = BeautifulSoup(html, "html5lib")
    return soup.find_all('input')[2]['value']

def requests1():
    url = "http://one.ccnu.edu.cn/"

    headers = {
	'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	'accept-encoding': "gzip, deflate",
	'accept-language': "en,zh-CN;q=0.9,zh;q=0.8",
	'cache-control': "no-cache",
	'connection': "keep-alive",
	'host': "one.ccnu.edu.cn",
	'pragma': "no-cache",
	'upgrade-insecure-requests': "1",
	'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
	'postman-token': "473bffe7-9c72-a82b-bfb8-44795ab87dee"
	}

    session = requests.Session()
    session.max_redirects = 0
    r = session.get(url, headers = headers)
    print(r.headers)
    cookie = r.headers['Set-Cookie']
    
    rpstart = cookie.find("Httponly")
    jid = getjid(cookie)
    routeportal = getjid(cookie[rpstart:-1])
    return jid, routeportal

def requests2(jid1, routeportal):
    url = "http://one.ccnu.edu.cn/cas/login_portal;jsessionid=" + jid1
    headers = {
	'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	'accept-encoding': "gzip, deflate",
	'accept-language': "en,zh-CN;q=0.9,zh;q=0.8",
	'cache-control': "no-cache",
	'connection': "keep-alive",
	'cookie': "JSESSIONID="+ jid1 +"; routeportal=" + routeportal,
	'host': "one.ccnu.edu.cn",
	'pragma': "no-cache",
	'upgrade-insecure-requests': "1",
	'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
	'postman-token': "81e64ece-3133-74d8-c316-89b2f42cf311"
	}
    session = requests.Session()
    r = session.get(url, headers = headers)
    print(r.headers)
    cookie = r.headers['Set-Cookie']
    jid2 = getjid(cookie)
    ltid = getltid(r.text)
    print(ltid)
    return jid2, ltid

def get_strange(jid1, jid2, ltid):
    url = "https://account.ccnu.edu.cn/cas/login;jsessionid=" + jid2
    querystring = {
        "service": "http://one.ccnu.edu.cn/cas/login_portal;jsessionid=" + jid1
    }
    headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en,zh-CN;q=0.9,zh;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'content-length': "151",
    'content-type': "application/x-www-form-urlencoded",
    'cookie': "JSESSIONID=" + jid2,
    'host': "account.ccnu.edu.cn",
    'origin': "https://account.ccnu.edu.cn",
    'pragma': "no-cache",
    'referer': "https://account.ccnu.edu.cn/cas/login?service=http%3A%2F%2Fone.ccnu.edu.cn%2Fcas%2Flogin_portal%3Bjsessionid%3D" + jid1,
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
    }
    payload = {
        "username":"*",
        "password":"*",
        "lt":ltid,
        "execution":"e1s1",
        "_eventId":"submit",
        "submit":"LOGIN"
    } 
    session = requests.Session()
    session.max_redirect = 0
    r = session.post(url, headers = headers, params = querystring, data = payload)
    print(r.status_code) 
    
if __name__ == '__main__':
    jid1, routeportal = requests1()
    sleep(1)
    jid2, ltid = requests2(jid1, routeportal)
    sleep(1)
    print("jid1:" + jid1 + '\n' + "jid2:" + jid2 + '\n')
    get_strange(jid1, jid2, ltid)
