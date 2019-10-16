from test_case.test_loginCase import Login_Case
from test_case.online_case.test_online_ykb_case import Online_Ykb_Case
from test_case.leaguer_case.test_leaguer_level_case import Leaguer_Level_Case
from test_case.goods_case.test_goods_category_case import Goods_Category_Case
from test_case.goods_case.test_goods_case import Goods_Case
from common import config_manage, send_email
from common.send_dingding import send_ding
import unittest, HTMLTestRunner, time

'''自定义运行测试用例'''
login = unittest.TestLoader().loadTestsFromTestCase(Login_Case)
online = unittest.TestLoader().loadTestsFromTestCase(Online_Ykb_Case)
leaguer_level = unittest.TestLoader().loadTestsFromTestCase(Leaguer_Level_Case)
goods_category = unittest.TestLoader().loadTestsFromTestCase(Goods_Category_Case)
goods = unittest.TestLoader().loadTestsFromTestCase(Goods_Case)

if __name__ == '__main__':
    # suites = unittest.TestSuite([online_test, login_test, leaguer_level_test])
    suites = unittest.TestSuite()
    suites.addTests(leaguer_level)
    suites.addTests(goods_category)
    suites.addTests(goods)

    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # html_file = config_manage.REPORT_PATH + now + ".html"  #每次生成一份新的测试报告
    html_file = config_manage.REPORT_PATH + "TestResult_Report.html"  # 固定生成一份测试报告
    with open(html_file, "wb") as file:
        '''retry，指定重试次数，如果save_last_try 为True ，一个用例仅显示最后一次测试的结果,为False，则显示所有重试的结果'''
        runner = HTMLTestRunner.HTMLTestRunner(stream=file, title='游乐宝_Web自动化测试报告', description='用例执行情况:', verbosity=2,
                                               retry=0, save_last_try=False)
        runner.run(suites)
        # file.close()
    # send_ding("ui自动化测试结束")
    # send_email.send_Email()
