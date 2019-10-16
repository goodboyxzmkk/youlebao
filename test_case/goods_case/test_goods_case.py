import unittest
from ddt import ddt, data
from po.pages.goods_menu.goods_page import Goods_Page
from test_case.base_case import Base_Case
from common.get_random_info import RandomData

rd = RandomData()
test_data = [{'商品名称': rd.rd_str("商品名称"), '商品条码': rd.rd_pystr(15), '售卖价格': 10, '初始化库存': 0,
              '库存预警数量': 50, '估算成本': 10, '退货手续费': 1, '预期结果': '保存成功'},
             {'商品名称': rd.rd_str("商品名称"), '商品条码': rd.rd_pystr(15), '售卖价格': 10, '初始化库存': 0,
              '库存预警数量': 50, '估算成本': 10, '退货手续费': 1, '预期结果': '保存成功'}]


@ddt
class Goods_Case(Base_Case):
    # @unittest.skip("跳过")
    @data(*test_data)
    def test_001_goods_add(self, data):
        '''添加通用商品'''
        super().default_login()
        goods_page = Goods_Page(self.base, data)
        goods_page.switch_in_goods_menu()
        goods_page.click_add_btn()
        goods_page.click_goods_btn()
        goods_page.input_goods_info()
        goods_page.click_save_btn()
        goods_page.assert_add_info()

    @unittest.skip("跳过")
    def test_002_select_group(self):
        super().default_login()
        goods_page = Goods_Page(self.base, data)
        goods_page.switch_in_goods_menu()
        goods_page.click_add_btn()
        goods_page.click_goods_btn()

        # goods_page.select_group()


if __name__ == '__main__':
    unittest.main()
