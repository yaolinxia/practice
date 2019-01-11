# -*- coding: utf-8 -*-
# ** Project : sa_qa
# ** Created by: Yizhen
# ** Date: 2018/11/19
# ** Time: 9:22

from flask import Blueprint
from flask_restplus import Resource, Api, Namespace

# wyz_blueprint = Blueprint('wyz', __name__)
# wyz_api = Api(wyz_blueprint)

api = Namespace('wyz',description='wyz namespace')

@api.route("/wyz")
class Wyz(Resource):
    """Show a single todo item and lets you delete them"""

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
