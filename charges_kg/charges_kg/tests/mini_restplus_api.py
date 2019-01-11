# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/28
# ** Time: 11:24


from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=5010,debug=True)
