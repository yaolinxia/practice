# -*- coding: utf-8 -*-
# ** Project : sa_qa
# ** Created by: Yizhen
# ** Date: 2018/11/19
# ** Time: 9:22
import operator
from decimal import Decimal

import numpy as np
from flask import jsonify
from flask_restplus import Resource, Namespace, fields

from ml.charge_recognition.charge_test import sentence2vec, model, index2label
from web.validators.forms import ChargeForm

api = Namespace('charge', description="(刑事)罪名预测引擎")

# Argument parsers
parser = api.parser()
parser.add_argument('sentence', required=True, help='描述的文本', location='args')  # , default='喝酒开车'

rst = {
    "errorCode": 0,
    "msg": "返回成功",
    "data": None
}

charge = api.model('charge', {
    'sentence': fields.String(required=True, description='描述的文本'),  # , default='喝酒开车'
})

@api.route("/")
class Charge(Resource):
    """
    （刑事）罪名预测引擎
    """
    @api.expect(parser)
    def get(self):
        """
        罪名预测
        根据用户的输入预测罪名
        """
        args = parser.parse_args()
        sentence = args.get('sentence')
        return jsonify(rst)

    @api.expect(charge)
    def post(self):
        """
        罪名预测
        根据用户的输入预测罪名
        """
        form = ChargeForm().validate_for_api()
        sentence = form.sentence.data
        return jsonify(rst)
