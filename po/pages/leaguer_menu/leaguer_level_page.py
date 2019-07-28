# coding:utf-8
from selenium.webdriver.common.by import By
from common import config_manage
from common.sql_helper import Sql_Helper
from po.pages.base_page import Base_Page

leaguer_level_loc = config_manage.get_yaml_page_loc('leaguer_loc\\leaguer_level_loc.yaml')


class Leaguer_Level_Page():
    def __init__(self, base_page, test_data):
        try:
            if isinstance(base_page, Base_Page):
                self.base = base_page
        except:
            print("base_page类型异常")
        self.data = test_data
        self.sql_assert = Sql_Helper()

    def switch_in_leaguer_level_menu(self):
        self.base.wait(1)
        self.base.click(By.XPATH, leaguer_level_loc["会员菜单"])
        self.base.click(By.XPATH, leaguer_level_loc["会员管理菜单"])
        self.base.wait(1)
        self.base.click(By.XPATH, leaguer_level_loc["会员级别菜单"])
        self.base.switch_in_iframe(leaguer_level_loc["右侧iframe"])
        self.base.wait(2)

    def click_add_btn(self):
        self.base.click(By.XPATH, leaguer_level_loc["新增按键"])

    def input_add_info(self):
        self.base.input(By.XPATH, leaguer_level_loc["级别名称"], self.data["级别名称"])
        self.base.clear_and_input(By.XPATH, leaguer_level_loc["续期价格"], self.data["续期价格"])
        self.base.clear_and_input(By.XPATH, leaguer_level_loc["补卡价格"], self.data["补卡价格"])
        self.base.clear_and_input(By.XPATH, leaguer_level_loc["积分过期时长"], self.data["积分过期时长"])
        self.base.clear_and_input(By.XPATH, leaguer_level_loc["注销退款系数"], self.data["注销退款系数"])
        self.base.clear_and_input(By.XPATH, leaguer_level_loc["换卡价格"], self.data["换卡价格"])
        self.base.input(By.XPATH, leaguer_level_loc["备注"], self.data["备注"])
        self.base.wait(2)

    def click_save_btn(self):
        self.base.click(By.XPATH, leaguer_level_loc["保存按键"])

    def assert_add_result(self):
        assert self.base.exists_element(By.XPATH, leaguer_level_loc["保存提示"]) == True
        text = self.base.get_text(By.XPATH, leaguer_level_loc["保存提示"])
        self.base.log.info("【保存提示文本】:" + str(text))
        sql = leaguer_level_loc["sql断言"] + "'" + self.data["级别名称"] + "'"
        result = self.sql_assert.ExecQuery(sql)  # 返回list
        self.base.log.info("【数据库检查结果】:" + str(result))
        assert result is not None
        assert result[0]['LevelName'] == self.data["级别名称"]

    def input_query_level_name(self):
        self.base.input(By.XPATH, leaguer_level_loc["查询级别名称"], self.data["级别名称"])

    def click_query_btn(self):
        self.base.click(By.XPATH, leaguer_level_loc["查询按键"])

    def assert_query_result(self):
        self.base.wait(1)
        result = self.base.get_col_text(By.XPATH, leaguer_level_loc["查询table"], 0, 1)
        self.base.wait(1)
        assert result == self.data["级别名称"]

    def click_query_checkbox(self):
        self.base.wait(1)
        self.base.click(By.XPATH, leaguer_level_loc["选择框"])

    def click_del_btn(self):
        self.base.click(By.XPATH, leaguer_level_loc["删除按键"])
        self.base.wait(2)

    def click_del_is_okbtn(self):
        self.base.switch_out_iframe()
        self.base.click(By.XPATH, leaguer_level_loc["确认删除"])

    def assert_del_result(self):
        self.base.switch_in_iframe(leaguer_level_loc["右侧iframe"])
        assert self.base.exists_element(By.XPATH, leaguer_level_loc["保存提示"]) == True
        result = self.base.get_text(By.XPATH, leaguer_level_loc["保存提示"])
        self.base.log.info("【保存提示文本】:" + str(result))
        assert result.find("数据删除成功")  # 判断字符串是否包含子字符串
