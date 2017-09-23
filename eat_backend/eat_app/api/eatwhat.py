#coding:utf-8
from flask import jsonify ,request
from . import api
import json
import os
from random import randint

@api.route('/eatwhat/', methods = ['GET'])
def eatwhat():
    items = ['东一', '东二', '学子', '桂香园', '博雅园', '外卖']
    item = items[randint(0, 5)]
    return jsonify({
        "location": item
    })
