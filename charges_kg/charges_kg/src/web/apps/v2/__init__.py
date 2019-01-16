# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/28
# ** Time: 11:32
from flask import Blueprint
from flask_restplus import Api
from web.apps.v2.wyz import api as ns_wyz
from web.apps.v2.yyx import api as ns_yyx

blueprint = Blueprint('v2', __name__, url_prefix='/api/v2')
api = Api(blueprint, title='Charge predict', version='2.0', description='A description')

api.add_namespace(ns_wyz)
api.add_namespace(ns_yyx)