import unittest
from ddt import ddt, data
from po.pages.goods_menu.goods_page import Goods_Page
from test_case.base_case import Base_Case
from common.get_random_info import RandomData


random_str = RandomData()
test_data = [{'商品名称': random_str.get_random_str("商品名称"), '商品条码': random_str.random_pystr(15), '售卖价格': 10, '初始化库存': 0,
              '库存预警数量': 50, '估算成本': 10, '退货手续费': 1},
             {'商品名称': random_str.get_random_str("商品名称"), '商品条码': random_str.random_pystr(15), '售卖价格': 10, '初始化库存': 0,
              '库存预警数量': 50, '估算成本': 10, '退货手续费': 1}]


@ddt
class Goods_Case(Base_Case):
    # @unittest.skip("跳过")
    @data(*test_data)
    def test_001_goods_category_add(self, data):
        '''添加通用商品'''
        super().default_login()
        goods_page = Goods_Page(self.base, data)
        goods_page.switch_in_goods_menu()
        goods_page.click_add_btn()
        goods_page.click_goods_btn()
        goods_page.input_goods_info()
        goods_page.click_save_btn()


if __name__ == '__main__':
    unittest.main()
