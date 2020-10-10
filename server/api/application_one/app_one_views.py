from flask import Blueprint, request
from flask_restx import Api, Resource

# app = Flask(__name__)
# 创建蓝图
# app_one_api = Api(app=Blueprint('app_one_api', __name__))
app_one_api = Blueprint('app_one_api', __name__)
# 创建api接口 相当于一个独立的小型应用
api_one = Api(app_one_api)


# 建立路由  有了路由可以建立相应的网络请求链接  并且可以对同一个链接发送不同的请求  节省视图的创建
@api_one.route('/')
class Wss(Resource):

    # 接收get请求
    @staticmethod
    def get():
        print('hello world')
        return 'hello world'

    # 接收post请求
    @staticmethod
    def post():
        json_data = request.json
        print(json_data)
        return 'hello world'

    # 接收put请求
    @staticmethod
    def put():
        print('hello world')
        return 'hello world'


if __name__ == '__main__':
    import requests
    import json
    res_one = requests.get('http://127.0.0.1:5000/hello')
    res_two = requests.post('http://127.0.0.1:5000/hello', json=json.dumps({"a": "1"}))
    res_three = requests.put('http://127.0.0.1:5000/hello')
    print(res_one)
    print(res_two)
    print(res_three)

