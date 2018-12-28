# encoding = utf-8
import xlrd
from xlwt import *

# 读数据
def read_excel(path):
    # 定义一个列表，存放关键词
    keyword = []
    bk = xlrd.open_workbook(filename)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("工作表1")
    except:
        print("代码出错")
    # 获取行数
    nrows = sh.nrows
    for i in range(1, nrows):
        for s in sh.cell_value(i, 3).split(" "):
            if s and s not in keyword:
                keyword.append(s)
        # print(sh.cell_value(i, 3))
    # print(keyword)
    return keyword

# 将电子表格中的值，转成json格式，每一行对应一个json
def excel_to_json(path):
    # 定义一个列表，存放所有的dict
    dict_list = []
    bk = xlrd.open_workbook(filename)
    try:
        sh = bk.sheet_by_name("工作表1")
    except:
        print("代码出错")
    # 获取行数
    nrows = sh.nrows
    # 每一行都是一个dict,每一行新开一个dict
    for i in range(1, nrows):
        dict = {}
        # for j in range(0, 2):
        # print(sh.cell_value(i, j))
        dict["code"] = sh.cell_value(i, 0)
        dict["action"] = sh.cell_value(i, 1)
    # print(dict)
        dict_list.append(dict)
    print(dict_list)
        # for s in sh.cell_value(i, 3).split(" "):
        #     if s and s not in keyword:
        #         keyword.append(s)
        # print(sh.cell_value(i, 3))


if __name__ == '__main__':
    filename = "E:\yaolinxia\\files\\南京违法行为关键词抽取_yao改.xlsx"
    excel_to_json(filename)