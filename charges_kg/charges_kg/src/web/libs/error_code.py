# -*- coding: utf-8 -*-
# ** Project : domainqa
# ** Created by: Yizhen
# ** Date: 2018/8/17
# ** Time: 9:40
from web.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    errorCode = 0


class ReturnNone(APIException):
    code = 201
    msg = 'return null'
    errorCode = 0


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake !'
    errorCode = 999
    data = []


class RequestFailed(APIException):
    # 无法处理请求的方法
    code = 416
    msg = 'Processing request failed'
    errorCode = 1008


class ParameterException(APIException):
    # 传入参数异常
    code = 400
    msg = 'invalid parameter'
    errorCode = 1000


class NotFound(APIException):
    # 资源没有找到
    code = 404
    msg = 'the resource are not found !'
    errorCode = 1001


class AuthFailed(APIException):
    # 授权失败
    code = 401
    msg = 'authorization failed'
    errorCode = 1005


class Forbidden(APIException):
    # 禁止访问
    code = 403
    msg = 'forbidden, not in scope'
    errorCode = 1004
