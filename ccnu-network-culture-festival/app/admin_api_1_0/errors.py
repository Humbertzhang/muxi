# coding: utf-8
"""
    error.py
    `````````

    : HTTP 错误处理

"""

from flask import jsonify


def not_found(message):
    response = jsonify({'error': 'not_found', 'message': message})
    response.status_code = 404
    return response


def bad_request(message):
    response = jsonify({'error': 'bad_request', 'message': message})
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify({'error': 'unathorized', 'message': message})
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_code = 403
    return response


def server_error(message):
    response = jsonify({'error': 'server_error', 'message': message})
    response.status_code = 500
    return response
