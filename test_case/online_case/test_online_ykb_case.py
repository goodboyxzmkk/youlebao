# coding:utf-8
from test_case.base_case import Base_Case
from po.pages.online_menu.online_page import Online_Page
import unittest

test_data = [{'用户名': 'admin', '密码': 'admin', '预期结果': '超级管理员(admin)', '登录成功': '是'},
             {'用户名': 'admin', '密码': 'error', '预期结果': '用户密码错误（错误码:90002）', '登录成功': '否'}]

# @unittest.skip()
class Online_Ykb_Case(Base_Case):

    def test_001_online_ykb_case(self):
        super().default_login()
        online_page = Online_Page(self.base, test_data)
        online_page.switch_in_ykb_menu()
        self.flag = False


if __name__ == '__main__':
    unittest.main()
