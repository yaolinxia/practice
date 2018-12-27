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
# 关键词转list
# def to_list(path):


if __name__ == '__main__':
    filename = "F:\pycharm\yao\\files\\南京违法行为关键词抽取_yao改.xlsx"
    read_excel(filename)