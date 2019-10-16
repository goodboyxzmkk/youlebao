import unittest
from ddt import ddt, data
from test_case.base_case import Base_Case
from po.pages.goods_menu.goods_category_page import Goods_Category_Page
from common.get_random_info import RandomData

rd = RandomData()
test_data = [{'分类名称': '一级分类{}'.format(rd.rd_pystr(5)), '预期结果': '保存成功'}, ]
test_data2 = [{'分类名称': '二级分类{}'.format(rd.rd_pystr(5)), '预期结果': '保存成功'}, ]


@ddt
class Goods_Category_Case(Base_Case):

    @data(*test_data)
    def test_001_goods_category_add(self, data):
        '''添加一级分类'''
        super().default_login()
        goods_category_page = Goods_Category_Page(self.base, data)
        goods_category_page.switch_in_goods_category_menu()
        goods_category_page.click_all_goods_list()
        goods_category_page.click_add_btn()
        goods_category_page.input_info_add()
        goods_category_page.click_save_btn()
        goods_category_page.assert_add_info()

    @data(*test_data2)
    def test_002_goods_category_add(self, data):
        '''添加二级分类'''
        super().default_login()
        goods_category_page = Goods_Category_Page(self.base, data)
        goods_category_page.switch_in_goods_category_menu()
        goods_category_page.click_frist_goods_list()
        goods_category_page.click_add_btn()
        goods_category_page.input_info_add()
        goods_category_page.click_save_btn()
        goods_category_page.assert_add_info()


if __name__ == '__main__':
    unittest.main()
