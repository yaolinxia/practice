# -*- coding: utf-8 -*-
# ** Project : xknowledge
# ** Created by: Yizhen
# ** Date: 2018/7/24
# ** Time: 15:33

from datetime import date
from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from flask_cors import *

from config.config import ProductionConfig
from web.libs.error_code import ServerError
import logging
log = logging.getLogger(__name__)

class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        # 兼容其他的序列化
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()

class Flask(_Flask):
    json_encoder = JSONEncoder


def register_blueprint(app):
    """
    蓝图注册
    :param app:
    :return:
    """

    from web.apps import blueprint_list
    for bp in blueprint_list:
        app.register_blueprint(bp)

        log.info('>>>>> Starting Swagger at http://{0}{1}/ <<<<<'.format(app.config['SERVER_NAME'],bp.url_prefix))

def create_app(config=ProductionConfig):
    """
    创建app应用
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app, supports_credentials=True)
    register_blueprint(app)  # 调用注册蓝图函数
    return app
