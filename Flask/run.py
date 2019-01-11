# -*- coding: utf-8 -*-
# run.py
from flask import Flask, render_template, request
from flask_flatpages import FlatPages

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_ROOT = 'pages'
FLATPAGES_EXTENSION = '.md'


app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)

@app.route('/')
def index():
    return "hello"
    # pass  # 为了方便演示这里省略详细代码

@app.route('/list/<string:tag>/')
def page_list(tag):
    pass

@app.route('/page/<string:uri>/')
def page(uri):
    pass

# 新增的后台部分代码
from adminPages import admin
app.register_blueprint(admin, url_prefix='/admin')

if __name__ == '__main__':
    app.run()