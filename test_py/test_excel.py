#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from xlwt import *

# 指定以utf-8格式打开
file = Workbook(encoding='utf-8')
# 指定打开的文件名
table = file.add_sheet('data')

# 字典数据
data = {
    "1": ["张三", 150, 120, 100],
    "2": ["李四", 90, 99, 95],
    "3": ["王五", 60, 66, 68]
}

list_data = []

# for 循环
num = [a for a in data]
# 字典数据取出后，先排序
# print(num)
num.sort()
print(num)

for x in num:
    # 讲字符串转为整数
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    list_data.append(t)
# print(t)
print(list_data)

for i, p in enumerate(list_data):
    # 讲数据写入进文件中
    # print(i, p)
    for j, q in enumerate(p):
        # print(i, j, p)
        table.write(i, j, q)

file.save('data.xlsx')

