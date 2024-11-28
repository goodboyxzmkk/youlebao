# coding:utf-8
from selenium.webdriver.common.by import By
from common import config_manage

online_loc = config_manage.get_yaml_page_loc('online_loc/online_loc.yaml')


class Online_Page():
    def __init__(self, Base_Page, test_data):
        self.base = Base_Page
        self.data = test_data

    def switch_in_ykb_menu(self):
        self.base.click(By.XPATH, online_loc["线上页面"]["线上"])
        self.base.switch_in_iframe(online_loc["线上页面"]["线上渠道iframe"])
        self.base.wait(2)
        self.base.click(By.XPATH, online_loc["线上页面"]["线上渠道"])
        self.base.switch_out_iframe()
        self.base.switch_in_iframe(online_loc["线上页面"]["盈客宝管理iframe"])
        self.base.click(By.XPATH, online_loc["线上页面"]["盈客宝管理"])
