import os

import requests
import json

# 定义请求url
import xlwt

url = "https://movie.douban.com/j/search_subjects"
# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
# 循环构建请求参数并且发送请求
for page_start in range(0, 100, 20):
    params = {
        "type": "movie",
        "tag": "热门",
        "sort": "recommend",
        "page_limit": "20",
        "page_start": page_start
    }
    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )
    # 方式一:直接转换json方法
    # results = response.json()
    # 方式二: 手动转换
    # 获取字节串
    content = response.content
    # 转换成字符串
    string = content.decode('utf-8')
    # 把字符串转成python数据类型
    results = json.loads(string)
    # 解析结果

    path = 'd:/data.xls'
    # 创建Workbook，相当于创建Excel
    if os.path.exists(path):

        book = xlwt.Workbook(encoding='utf-8')
        # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
        sheet = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)
        book.save("d:/data.xls")  # 保存工作簿
    else:
        book = xlwt.Workbook(encoding='utf-8')
        # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
        sheet = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)
        for i in range(len(results['subjects'])):
            for movie in results['subjects']:
                sheet.write(i, 0, movie["title"])  # 像表格中写入数据（对应的行和列）
                sheet.write(i, 1, movie["rate"])
                print(movie["title"], movie["rate"])
                book.save("d:/data.xls")  # 保存工作簿
print("xls格式表格写入数据成功！")
