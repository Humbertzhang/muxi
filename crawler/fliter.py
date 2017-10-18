import requests
from bs4 import BeautifulSoup
import re
from time import sleep
import pprint

head = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

apps = {}
content = []
for i in range(1,40):
    r = requests.get('http://app.mi.com/topList?page=' + str(i), headers = head)
    soup = BeautifulSoup(r.text)
    with open('hotapp.html', 'w') as f:
        f.writelines(soup.get_text("\n", strip=True))
    with open('hotapp.html', 'r') as f:
        html = f.readlines()

    content += html[12:108]
    sleep(0.2)

content = content[::-1]
record = 0
gametypes = ['模拟经营',  '动作枪战', '格斗快打', '体育运动', '跑酷闯关', '网游RPG', '战争策略', '赛车体育',  '棋牌桌游', '塔防迷宫', '儿童益智', '飞行空战', 'VR']
apps["游戏"] = []

for i in range(len(content)):
    if i % 2 == 0:
        record = content[i].rstrip('\n')
        if record not in apps.keys() and record not in gametypes:
            apps[record] = []
    elif i % 2 == 1:
        if record in gametypes:
            apps["游戏"].append(content[i].rstrip('\n'))
        else:
            apps[record].append(content[i].rstrip('\n'))

pprint.pprint(apps)
pprint.pprint(apps.keys())
