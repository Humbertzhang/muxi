import requests

r = requests.get("http://app.mi.com/categotyAllListApi?page=0&categoryId=23&pageSize=10000")

text = r.text

appinfo = text.split('}')
appnames = []
for item in appinfo:
    start = item.find('displayName') + 14
    end = item.find('icon') - 3
    name = item[int(start):int(end)] + '\n'
    if end > 0:
        appnames.append(name)

with open('游戏-休闲创意.data', 'w') as f:
    f.writelines(appnames)
