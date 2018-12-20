#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json

# 网上方法，测试下json读取文件
josn_path = "H:\python-workspace\qindun\extract_traffic_event\event_count_1210_add.json"
addrsfile = open(json, "r")
addrJson = json.loads(addrsfile.read())
addrsfile.close()
if addrJson:
    print("yes")