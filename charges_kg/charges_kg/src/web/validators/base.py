# -*- coding: utf-8 -*-
# ** Project : xknowledge
# ** Created by: Yizhen
# ** Date: 2018/11/2
# ** Time: 16:13

from flask import request
from wtforms import Form

from ...web.libs.error_code import ParameterException, RequestFailed


class BaseForm(Form):
    def __init__(self):
        # data = request.json  # 直接获取客户端传入的参数
        if request.method == 'POST':
            data = request.json
        elif request.method == 'GET':
            data = request.args.to_dict()
        else:
            raise RequestFailed(msg=self.errors)
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):  # 覆盖 Form 的validate方法
        valid = super(BaseForm, self).validate()
        if not valid:  # form errors 所有错误信息都存放在这里面
            raise ParameterException(msg=self.errors)
        return self
