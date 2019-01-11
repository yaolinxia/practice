# -*- coding: utf-8 -*-
# ** Project : sa_qa
# ** Created by: Yizhen
# ** Date: 2018/11/19
# ** Time: 9:21
from flask import Blueprint
from flask_restplus import Api

from web.apps.v1.charge import api as ns_charge

blueprint = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(blueprint, title='charge', version='1.0', description='（刑事）罪名预测引擎，基于罪名知识图谱，用于做罪名预测，并依据知识图谱解释预测结果',default='charge')

api.add_namespace(ns_charge)
