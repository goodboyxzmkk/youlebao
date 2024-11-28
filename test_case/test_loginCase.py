from test_case.base_case import Base_Case
from po.pages.login_page import Login_Page
from common import config_manage
from ddt import ddt, data
import unittest

test_data = [{'用户名': 'admin', '密码': 'admin', '预期结果': '超级管理员(admin)', '登录成功': '是'},
             {'用户名': 'admin', '密码': 'error', '预期结果': '账号或密码错误（错误码:8013）', '登录成功': '否'}]


@ddt
class Login_Case(Base_Case):

    @data(*test_data)
    def test_001_login_case(self, data):
        '''用户登录'''
        login_page = Login_Page(self.base, data)
        login_page.run_login()


if __name__ == '__main__':
    unittest.main()
