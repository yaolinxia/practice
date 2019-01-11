# -*- coding: utf-8 -*-
# ** Project : charges_kg
# ** Created by: Yizhen
# ** Date: 2018/12/24
# ** Time: 14:12
import glob
import json
from os.path import join as path_join

import os

from collections import defaultdict
from tqdm import tqdm

from ..config.config import RESOURCE_DIR
charges = []
with open(path_join(RESOURCE_DIR,'charges.txt'),'r',encoding='utf-8') as f:
    for line in f:
        charges.append(line.strip())

# print(len(charges))
#
# charges_all = []
# with open(r'E:\CAIL2018_ALL_DATA\meta\accu.txt','r',encoding='utf-8') as f:
#     for line in f:
#         charges_all.append(line.strip())
#
# print(len(charges_all))
#
# for item in (set(charges) &set(charges_all)):
#     print(item)


# all_charges = []
# with open(path_join(RESOURCE_DIR,'train.json'),'w',encoding='utf-8') as fw:
#     for fn in tqdm(glob.glob(r'E:\CAIL2018_ALL_DATA\*\*')):
#         file_name = os.path.basename(fn)
#         if file_name.endswith('json'):
#             with open(fn,'r',encoding='utf-8') as f:
#                 for line in f:
#                     data = json.loads(line)
#                     accusation = data.get('meta').get('accusation') # 罪名
#                     fact = data.get('fact')
#                     for acc in accusation:
#                         if acc in set(charges):
#                             fw.write(json.dumps(dict(fact=fact,charges=acc),sort_keys=True,ensure_ascii=False)+'\n')

charges_dict = defaultdict(int)
with open(path_join(RESOURCE_DIR,'train.json'),'r',encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        charges_dict[data.get('charges')] += 1
print(charges_dict)