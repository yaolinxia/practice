# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/29
# ** Time: 10:57

from flask import Flask, json, Blueprint
from flask_restplus import Resource, Api, Namespace

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:8888'

blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')

api = Api(blueprint,description='Api_description',version='1.0', name='Api_name',title='Api_title',default='Api_default')
ns = Namespace('Namespace', description="Namespace_description")
api.add_namespace(ns)
app.register_blueprint(blueprint)


@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


with app.app_context():
    urlvars = False  # Build query strings in URLs
    swagger = False  # Export Swagger specifications
    data = api.as_postman(urlvars=urlvars, swagger=swagger)
    fw = open('postman_import.json', 'w',encoding='utf-8')
    fw.write(json.dumps(data,ensure_ascii=False,sort_keys=True))