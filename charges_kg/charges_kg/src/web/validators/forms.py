# -*- coding: utf-8 -*-
# ** Project : xknowledge
# ** Created by: Yizhen
# ** Date: 2018/11/2
# ** Time: 16:14
from wtforms import StringField
from wtforms.validators import DataRequired

from ...web.validators.base import BaseForm as Form


class ChargeForm(Form):
    sentence = StringField("sentence", validators=[DataRequired(message="'sentence'缺失")])
    # sent = StringField("sent", validators=[DataRequired(message="'sent'缺失")])
