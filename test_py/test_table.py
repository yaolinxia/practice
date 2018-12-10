#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import xlwt, xlrd
from xlutils.copy import copy

def write_to_excel(sheet_name):
    file_name = 'test_1.xls'
    if not os.path.exists(file_name):
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet(sheet_name,cell_overwrite_ok=True)
        workbook.save(file_name)

    rb = xlrd.open_workbook(file_name)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    # 新的sheet页面
    worksheet = wb.add_sheet(sheet_name,cell_overwrite_ok=True)
    worksheet.write(0,0,'test')
    wb.save(file_name)

if __name__ == '__main__':
    for x in range(3):
        write_to_excel(x)
