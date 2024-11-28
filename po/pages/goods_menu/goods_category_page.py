from selenium.webdriver.common.by import By

from common import config_manage
from common.sql_helper import Sql_Helper
from po.pages.base_page import Base_Page

goods_category_loc = config_manage.get_yaml_page_loc("goods_loc/goods_category_loc.yaml")


class Goods_Category_Page():
    '''商品分类'''

    def __init__(self, base_page, test_data):
        try:
            if isinstance(base_page, Base_Page):
                self.base = base_page
        except:
            self.base.log("base_page异常!")
        self.data = test_data
        self.sql_assert = Sql_Helper()

    def switch_in_goods_category_menu(self):
        self.base.wait(1)
        self.base.click(By.XPATH, goods_category_loc["商品菜单"])
        self.base.click(By.XPATH, goods_category_loc["商品管理菜单"])
        self.base.wait(1)
        self.base.click(By.XPATH, goods_category_loc["商品资料菜单"])
        self.base.switch_in_iframe(goods_category_loc["右侧iframe"])
        self.base.wait(2)

    def click_all_goods_list(self):
        self.base.click(By.XPATH, goods_category_loc["所有商品分类"])

    def click_frist_goods_list(self):
        self.base.click(By.XPATH, goods_category_loc["第一个一级分类"])

    def click_add_btn(self):
        self.base.click(By.XPATH, goods_category_loc["新增子类"])

    def input_info_add(self):
        self.base.wait(2)
        self.base.input(By.XPATH, goods_category_loc["分类名称"], self.data["分类名称"])

    def click_save_and_add_btn(self):
        self.base.click(By.XPATH, goods_category_loc["保存并新增"])

    def click_save_btn(self):
        self.base.click(By.XPATH, goods_category_loc["保存"])
        self.base.wait(2)

    def assert_add_info(self):
        self.base.assert_alert_info(expect_value=self.data['预期结果'])
        result = self.sql_assert.ExecQuery(goods_category_loc['sql断言'] + "'" + self.data["分类名称"] + "'")
        self.base.log.info("数据库检查结果：{}".format(result))
        assert result[0]['ClassName'] == self.data['分类名称']
