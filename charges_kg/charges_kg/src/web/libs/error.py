# -*- coding: utf-8 -*-
# ** Project : domainqa
# ** Created by: Yizhen
# ** Date: 2018/8/17
# ** Time: 9:33
from flask import request, json
from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake'
    errorCode = 999

    def __init__(self, msg=None, code=None, errorCode=None, data=None, headers=None):
        if code:
            self.code = code
        if errorCode:
            self.errorCode = errorCode
        if msg:
            self.msg = msg
        if data:
            self.data = data
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            errorCode=self.errorCode,
            request=request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')

        return main_path[0]

    def get_headers(self, environ=None):
        """
        Get a list of headers.
        :param environ:
        :return:
        """
        return [('Content-Type', 'application/json')]
