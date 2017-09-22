from flask import jsonify ,request
from . import api
import json
import os
from random import randint

@api.route('/eatwhat/', methods = ['GET'])
def eatwhat():
        items = ['dongyi', 'donger', 'xuezi', 'guixiangyuan','boyayuan','waimai']
        item = items[randint(0,5)]
        return item
