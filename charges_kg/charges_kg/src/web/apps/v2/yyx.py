# -*- coding: utf-8 -*-
# ** Project : sa_qa
# ** Created by: Yizhen
# ** Date: 2018/11/19
# ** Time: 9:22

from flask import Blueprint
from flask_restplus import Namespace,Resource, Api

# yyx_blueprint = Blueprint('yyx', __name__)
# yyx_api = Api(yyx_blueprint, description="yyx_blueprint")

api = Namespace('yyx', description="yyx namespace")
@api.route("/yyx")
class yyx(Resource):
    def get(self):
        """
        GET
        """
        return {'hello': 'world'}

    def post(self):
        """
        POST
        """

        return {'hello': 'world'}
