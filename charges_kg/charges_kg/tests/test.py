# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/26
# ** Time: 17:21

import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = dict(sorted(x.items(), key=operator.itemgetter(1),reverse=True))

print(sorted_x)