# -*- coding: utf-8 -*-
# ** Project : sa_qa
# ** Created by: Yizhen
# ** Date: 2018/11/19
# ** Time: 9:36

import os
import sys

from config.config import ProductionConfig

src_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
domain_path = os.path.dirname(src_path)
web_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, src_path)
sys.path.insert(0, web_path)
sys.path.insert(0, domain_path)

from werkzeug.exceptions import HTTPException

from web.libs.error import APIException
from web.libs.error_code import ServerError
from web import create_app

app = create_app(ProductionConfig)

@app.errorhandler(Exception)
def framework_error(e):  # 全局捕获错误
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):  # 请求url错误
        code = e.code
        msg = e.description
        errorCode = 1007
        return APIException(msg=msg, code=code, errorCode=errorCode)
    else:  # 服务器内部错误
        print("ERROR: {}".format(e))
        return ServerError()

if __name__ == '__main__':
    app.run(threaded=True)
