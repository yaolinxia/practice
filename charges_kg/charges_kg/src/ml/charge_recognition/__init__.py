# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/25
# ** Time: 9:15

import os

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

MODEL_PATH = os.path.join(_ROOT, "resources", "ml", os.path.basename(os.path.dirname(os.path.realpath(__file__))))

