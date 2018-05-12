# coding: utf-8
from flask import Blueprint

admin_api = Blueprint(
    'admin_api',
    __name__,
    template_folder = 'templates',
    static_folder = 'static'
)

from . import views,authentication