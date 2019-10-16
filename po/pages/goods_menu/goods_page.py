from selenium.webdriver.common.by import By

from common import config_manage
from common.sql_helper import Sql_Helper
from po.pages.base_page import Base_Page

goods_loc = config_manage.get_yaml_page_loc("goods_loc\\goods_loc.yaml")


class Goods_Page():
    '''商品分类'''

    def __init__(self, base_page, test_data):
        try:
            if isinstance(base_page, Base_Page):
                self.base = base_page
        except:
            self.base.log.info("base_page异常!")
        self.data = test_data
        self.sql_assert = Sql_Helper()

    def switch_in_goods_menu(self):
        self.base.wait(1)
        self.base.click(By.XPATH, goods_loc["商品菜单"])
        self.base.click(By.XPATH, goods_loc["商品管理菜单"])
        self.base.wait(1)
        self.base.click(By.XPATH, goods_loc["商品资料菜单"])
        self.base.switch_in_iframe(goods_loc["右侧iframe"])
        self.base.wait(2)

    def click_add_btn(self):
        self.base.click(By.XPATH, goods_loc["新增按键"])

    def click_goods_btn(self):
        self.base.wait(2)
        self.base.click(By.XPATH, goods_loc["通用商品"])

    def input_goods_info(self):
        self.base.input(By.XPATH, goods_loc['商品名称'], self.data["商品名称"])
        self.base.input(By.XPATH, goods_loc['商品条码'], self.data["商品条码"])
        self.base.input(By.XPATH, goods_loc['售卖价格'], self.data["售卖价格"])
        if int(self.data['初始化库存']) > 0:
            self.base.input(By.XPATH, goods_loc['初始化库存'], self.data["初始化库存"])
        self.base.clear_and_input(By.XPATH, goods_loc['库存预警数量'], self.data["库存预警数量"])
        self.base.input(By.XPATH, goods_loc['估算成本'], self.data["估算成本"])
        self.base.input(By.XPATH, goods_loc['退货手续费'], self.data["退货手续费"])
        self.base.wait(1)

    def click_save_btn(self):
        self.base.click(By.XPATH, goods_loc["保存按键"])
        self.base.wait(2)

    def assert_add_info(self):
        self.base.assert_alert_info(expect_value=self.data['预期结果'])
        result = self.sql_assert.ExecQuery(goods_loc['sql断言'] + "'" + self.data["商品名称"] + "'")
        self.base.log.info("数据库检查结果：{}".format(result))
        assert result[0]['GoodName'] == self.data['商品名称']

    def select_group(self):
        self.base.wait(1)
        self.base.click(By.XPATH, '//*[@id="sltNormalGoodsClassAdd"]/div/div/input')
        eles = self.base.find_elements(By.XPATH, '//*[@id="sltNormalGoodsClassAdd"]/div/div/ul/li/a')
        self.base.wait(2)
        for ele in eles:
            ele.click()
            # print(ele.text)
