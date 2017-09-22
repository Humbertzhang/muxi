import unittest
from eat_app import create_app
from flask import current_app, url_for,jsonify
import random
import json

class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)
    
    def test_eatwhat(self):
        response = self.client.get(
            url_for('api.eatwhat', _external = True),
            content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
