# coding:utf-8
import xlrd, csv
from datetime import datetime
from xlrd import xldate_as_tuple
from common import config_manage


def get_data_excel(excelfile_Name, sheetName='Sheet1'):
    excelfile_path = config_manage.TESTDATA_PATH + excelfile_Name + ".xlsx"
    # excelfile_path = excelfile_Name
    book = xlrd.open_workbook(excelfile_path)
    table = book.sheet_by_name(sheetName)
    # 获取第一行作为key值
    keys = table.row_values(0)
    # 获取总行数
    rowNum = table.nrows
    # 获取总列数
    colNum = table.ncols
    if rowNum <= 1:
        print("总行数小于1")
    else:
        r = []
        j = 1
        for i in range(rowNum - 1):
            s = {}
            # 从第二行取对应values值
            values = table.row_values(j)
            for x in range(colNum):
                ctype = table.cell(j, x).ctype  # 表格的数据类型
                cell = table.cell_value(j, x)
                if ctype == 2 and cell % 1 == 0:  # 如果是整形
                    cell = int(cell)
                elif ctype == 3:
                    # 转成datetime对象
                    date = datetime(*xldate_as_tuple(cell, 0))
                    cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif ctype == 4:
                    cell = True if cell == 1 else False
                s[keys[x]] = cell
            r.append(s)
            j += 1
        return r


def get_data_csv(csvfile_Name):
    csvfile_path = config_manage.TESTDATA_PATH + csvfile_Name + '.csv'
    with open(csvfile_path, "r", encoding="gbk") as f:
        reader = csv.DictReader(f)
        column = [row for row in reader]
    return column


if __name__ == '__main__':
    filepath = "ddtt"
    print(get_data_excel(filepath))
