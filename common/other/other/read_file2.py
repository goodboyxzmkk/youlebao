# coding:utf-8
import xlrd, csv
from common import config_manage


def get_data_excel(excelfile_Name, sheetName='Sheet1'):
    excelfile_path = config_manage.TESTDATA_PATH + excelfile_Name + ".xlsx"
    # if excelfile_path.endswith('.xls') or file_path.endswith('.xlsx'):#判断文件是否为excel文件
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
                '''读excel数字类型默认读出来的是float,在把excel单元格设置为文本，或数字前加分号（'）'''
                s[keys[x]] = str(values[x])
            r.append(s)
            j += 1
        return r


def get_data_csv(csvfile_Name):
    csvfile_path = config_manage.TESTDATA_PATH + csvfile_Name + '.csv'
    with open(csvfile_path, "r", encoding="gbk") as f:
        reader = csv.DictReader(f)
        column = [row for row in reader]
    return column


if __name__ == "__main__":
    filepath = "d:\\ddt.xlsx"
    sheetName = "Sheet1"
    print(get_data_excel(filepath))
