# -*- coding: utf-8 -*-
# run.py
from flask import Flask, render_template, request
# flask_flatpages: 对于flask应用提供页面的集合
from flask_flatpages import FlatPages

FLATPAGES_AUTO_RELOAD = True
FLATPAGES_ROOT = 'pages'
FLATPAGES_EXTENSION = '.md'


app = Flask(__name__)
app.config.from_object(__name__)
flatpages = FlatPages(app)

# 首页
@app.route('/')
def index():
    return "hello"
    # pass

# 文章列表
@app.route('/list/<string:tag>/')
def page_list(tag):
    pass

# 文章详情
@app.route('/page/<string:uri>/')
def page(uri):
    pass

# 新增的后台部分代码
@app.route('/admin/login/')
def admin_login():
    pass

@app.route('/admin/page/')
def admin_pages():
    pass

@app.route('/admin/page/new/')
def new_page():
    pass

@app.route('/admin/page/edit/')
def edit_page():
    pass

if __name__ == '__main__':
    app.run()