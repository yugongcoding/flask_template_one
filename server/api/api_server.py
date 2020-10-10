# -*- coding: utf-8 -*-
from flask import Flask
from server.api.application_one.app_one_views import app_one_api
from server.api.application_two.app_two_views import app_two_api
import socket

api_server = Flask(__name__)
# 注册蓝图
api_server.register_blueprint(app_one_api)
api_server.register_blueprint(app_two_api)


if __name__ == '__main__':
    api_server.run(host='0.0.0.0', port=5000, debug=True)
