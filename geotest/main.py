from pymongo import MongoClient, GEO2D
from pprint import pprint

client = MongoClient()
db = client['geodb'] 
col = db['geocol']

db.col.create_index([("loc", GEO2D)])

def insertp(name, x, y):
    result = db.col.insert_one({"name": name, "loc":[x, y]})
    print(result.inserted_id)

# 离某个点最近的人
# 默认排序按照离给定点的远近来排
def findnearp(x, y):
    for doc in db.col.find({"loc":{"$near":[x, y]}}).limit(10):
        pprint(doc)

# 某个矩形范围内的人
# 默认为按离左上角距离(x1, y1) 来排
def findarea(x1, y1, x2, y2):
    query = {"loc": {"$within": {"$box": [[x1, y1], [x2, y2]] } } }
    for doc in db.col.find(query):
        pprint(doc)

# 某个圆形范围内的人
# 默认排序按圆心远近来排
def findcircle(x, y, r):
    query = {"loc": {"$within": {"$center": [[x, y], r]}}}
    for doc in db.col.find(query):
        pprint(doc)
