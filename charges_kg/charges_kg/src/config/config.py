# -*- coding: utf-8 -*-
import json
import os
from os.path import join as path_join

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    with open(os.path.join(BASE_DIR, 'src', 'config', 'config.json'), 'r', encoding='utf-8') as f:
        db_config = json.load(f)
except FileNotFoundError:
    print("db_config.json don't find")
    db_config = {}

DATABASE_CONF = db_config.get("DATABASES", None)

# 模型地址
MODEL_DIR = path_join(BASE_DIR, 'resources', 'models')

# sqa 模型地址
SQA_MODEL_DIR = path_join(MODEL_DIR, 'sqa_similarity')

# 资源地址
RESOURCE_DIR = path_join(BASE_DIR, 'resources')

# LTP model
if os.name == 'nt':
    LTP_MODEL_PATH = 'E:\\data\\ltp_local\\ltp-data-v3.3.1\\ltp_data'
else:
    LTP_MODEL_PATH = path_join(MODEL_DIR, 'ltp_data')


class Config(object):
    # Flask settings
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False

    # Flask-Restplus settings
    # RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    # RESTPLUS_VALIDATE = True
    # RESTPLUS_MASK_SWAGGER = False
    # RESTPLUS_ERROR_404_HELP = False

    # SQLAlchemy settings
    # DATABASE_URI = 'sqlite:///db.sqlite'
    # TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    SERVER_NAME = '0.0.0.0:5004'


class DevelopmentConfig(Config):
    DEBUG = True
    SERVER_NAME = '127.0.0.1:7000'
