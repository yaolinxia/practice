# -*- coding: utf-8 -*-
# ** Project : xknowledge
# ** Created by: Yizhen
# ** Date: 2018/11/2
# ** Time: 15:41

from web.apps.v1 import blueprint as api1
from web.apps.v2 import blueprint as api2

blueprint_list = [
    api1,
    api2,
]

