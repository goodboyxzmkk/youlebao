from selenium.webdriver.common.by import By
from common import config_manage
from po.pages.base_page import Base_Page

login_loc = config_manage.get_yaml_page_loc('login_loc.yaml')


class Login_Page():
    def __init__(self, base_page, test_data):
        if isinstance(base_page, Base_Page):
            self.base = base_page
        self.data = test_data

    def run_login(self):
        self.base.input(By.XPATH, login_loc['登录页面']['用户名'], self.data['用户名'])
        self.base.input(By.XPATH, login_loc['登录页面']['密码'], self.data['密码'])
        self.base.click(By.XPATH, login_loc['登录页面']['登录按键'])
        self.base.wait(2)
        if (self.data['登录成功'] == '是'):
            result = self.base.get_text(By.XPATH, login_loc['断言']['登录成功'])
        else:
            result = self.base.get_text(By.XPATH, login_loc['断言']['登录失败'])
        self.base.log.info("【实际结果】 ：" + result)
        self.base.log.info("【预期结果】 ：" + self.data['预期结果'])
        assert str(result).strip() == self.data['预期结果']
