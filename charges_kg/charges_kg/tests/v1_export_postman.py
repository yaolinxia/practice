# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/29
# ** Time: 16:41
from web.apps.v1 import blueprint, api


from flask import Flask,json
app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:8888'
app.register_blueprint(blueprint)

with app.app_context():
    urlvars = False  # Build query strings in URLs
    swagger = True  # Export Swagger specifications
    data = api.as_postman(urlvars=urlvars, swagger=swagger)
    fw = open('postman_import_v1.json', 'w',encoding='utf-8')
    fw.write(json.dumps(data,ensure_ascii=False,sort_keys=True))