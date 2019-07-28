import unittest
import time
import HTMLTestRunner

from common import send_email, config_manage
import os

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(start_dir=config_manage.TESTCASE_PATH,
                                                pattern='test_*.py',
                                                top_level_dir=None)  # 加载路径下的所有test开头的用例
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    # html_file = config_manage.REPORT_PATH + now + ".html"  #每次生成一份新的测试报告
    html_file = config_manage.REPORT_PATH + "TestResult_Report.html"  # 固定生成一份测试报告
    '''wb以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。'''
    fp = open(html_file, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='游乐宝_Web自动化测试报告', description='用例执行情况:')
    runner.run(suite)
    fp.close()

    # 发送邮件
    # send_email.send_Email()