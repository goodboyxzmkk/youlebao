# coding:utf-8
from test_case.base_case import Base_Case
from po.pages.leaguer_menu.leaguer_level_page import Leaguer_Level_Page
import unittest

test_data = {'级别名称': 'atuo级别', '续期价格': 10, '补卡价格': 10, '积分过期时长': 2, '注销退款系数': 1,
             '换卡价格': 2, '备注': '备注1', '预期结果': '保存成功'}


# @unittest.skip("跳过")
class Leaguer_Level_Case(Base_Case):

    # @unittest.skip("跳过")
    def test_001_leaguer_level_add(self):
        '''新增会员'''
        super().default_login()
        leaguer_level_page = Leaguer_Level_Page(self.base, test_data)
        leaguer_level_page.switch_in_leaguer_level_menu()
        leaguer_level_page.click_add_btn()
        leaguer_level_page.input_add_info()
        leaguer_level_page.click_save_btn()
        leaguer_level_page.assert_add_result()

    # @unittest.skip("跳过")
    def test_002_leaguer_level_query(self):
        '''查询会员'''
        super().default_login()
        leaguer_level_page = Leaguer_Level_Page(self.base, test_data)
        leaguer_level_page.switch_in_leaguer_level_menu()
        leaguer_level_page.input_query_level_name()
        leaguer_level_page.click_query_btn()
        leaguer_level_page.assert_query_result()

    # @unittest.skip("跳过")
    def test_003_leaguer_level_del(self):
        '''删除会员'''
        super().default_login()
        leaguer_level_page = Leaguer_Level_Page(self.base, test_data)
        leaguer_level_page.switch_in_leaguer_level_menu()
        leaguer_level_page.input_query_level_name()
        leaguer_level_page.click_query_btn()
        leaguer_level_page.click_query_checkbox()
        leaguer_level_page.click_del_btn()
        leaguer_level_page.click_del_is_okbtn()
        leaguer_level_page.assert_del_result()


if __name__ == '__main__':
    unittest.main()
