# coding:utf-8

import os, time
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from common import config_manage
from common.logger import Logger


class Base_Page(object):

    def __init__(self, driver, log):
        self.driver = driver
        try:
            if isinstance(log, Logger):
                self.log = log
        except:
            print("log类型不正确")
        self.timeout = 5
        self.t = 0.5

    def find_element(self, by, loc):
        # self.log.info("【find元素】，定位方式：{}, 定位表达式：{}".format(by, loc))
        self.highlight_element(by, loc)
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located((by, loc)))
        return ele

    def find_elements(self, by, loc):
        # self.log.info("【find元素】，定位方式：{}, 定位表达式：{}".format(by, loc))
        # presence_of_element_located 需要传元组类型
        eles = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located((by, loc)))
        return eles

    def exists_element(self, by, loc):
        '''判断元素是否存在'''
        try:
            self.driver.find_element(by, loc)
            return True
        except NoSuchElementException as e:
            return False

    def screenshot_img(self, methodName):
        '''错误截图'''
        file_path = config_manage.SCREEN_PATH
        date_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        img_name = file_path + date_time + ' ' + methodName + '.png'
        try:
            self.driver.get_screenshot_as_file(img_name)
            self.imgs.append(self.driver.get_screenshot_as_base64())
        except NameError as e:
            self.driver.get_windows_img()
        self.log.info("【异常截图路径】：" + img_name)

    def switch_handel(self):
        '''浏览器切换窗口'''
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)
        self.log.info("【浏览器切换窗口】")

    def input(self, by, loc, value):
        '''往输入框输入内容'''
        # self.driver.find_element(by, loc).send_keys(value)
        self.find_element(by, loc).send_keys(value)
        self.log.info("【输入】：{} , 定位方式：{} , 定位表达式：{}".format(value, by, loc))

    def clear(self, by, loc):
        '''清空输入框内容'''
        self.find_element(by, loc).clear()
        self.log.info("【清空元素文本】 , 定位方式：{} ， 定位表达式：{}".format(by, loc))

    def clear_and_input(self, by, loc, value):
        '''清空并输入内容'''
        self.find_element(by, loc).clear()
        self.find_element(by, loc).send_keys(value)
        self.log.info("【清空并输入】：{} , 定位方式：{} , 定位表达式：{}".format(value, by, loc))

    def input_and_KeyEnter(self, by, loc, value):
        '''输入并回车'''
        self.find_element(by, loc).send_keys(value)
        self.find_element(by, loc).send_keys(Keys.ENTER)
        self.log.info("【输入】：{} , 定位方式：{} , 定位表达式：{}".format(value, by, loc))

    def click(self, by, loc):
        '''点击元素'''
        self.find_element(by, loc).click()
        self.log.info("【点击元素】:  定位方式：{} ， 定位表达式：{}".format(by, loc))

    def highlight_element(self, by, loc):
        '''元素高亮显示'''
        ele = self.driver.find_element(by, loc)
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", ele,
                                   "background: yellow; border: 2px solid red;")

    def get_text(self, by, loc):
        '''获取文本 '''
        self.log.info("【获取元素文本】： 定位方式：{} ， 定位表达式：{}".format(by, loc))
        return self.find_element(by, loc).text

    def get_col_text(self, by, loc, row, col):
        '''传入table定位by,loc ，获取table中row行，col列的文本 '''
        table_ele = self.find_element(by, loc)
        try:
            rows = table_ele.find_elements_by_tag_name('tr')  # 返回list
            cols = rows[row].find_elements_by_tag_name("td")  # 返回list
            return cols[col].text
        except:
            return None
        self.log.info("【获取元素文本】： 定位方式：{} ， 定位表达式：{}".format(by, loc))

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def move_to_elemen_and_click(self, by, loc):
        '''移动鼠标悬停在某元素上并点击'''
        xm = self.find_element(by, loc)
        webdriver.ActionChains(self.driver).click(xm).perform()
        self.log.info("【鼠标悬停】在元素上并点击,定位方式：{} ， 定位表达式：{}".format(by, loc))

    def move_to_element(self, by, loc):
        '''鼠标悬停操作'''
        ele = self.find_element(by, loc)
        webdriver.ActionChains(self.driver).move_to_element(ele).perform()
        self.log.info("【鼠标悬停】在元素上,定位方式：{} ， 定位表达式：{}".format(by, loc))

    def switch_in_iframe(self, index_locator):
        # chrome浏览器——f12 ——console用于显示iframe个数
        # document.getElementsByTagName('iframe').length
        '''切入iframe,参数为索引或xpath定位'''
        try:
            if isinstance(index_locator, int):
                self.driver.switch_to.frame(index_locator)
                self.log.info("【切换iframe】,iframe索引：{}".format(index_locator))
            elif isinstance(index_locator, str):
                ele = self.driver.find_element_by_xpath(index_locator)
                self.driver.switch_to.frame(ele)
                self.log.info("【切换iframe】,iframe表达式：{}".format(index_locator))
        except:
            self.log.info("iframe切换异常")

    def switch_out_iframe(self):
        '''切出iframe'''
        self.driver.switch_to.default_content()
        self.log.info("【返回上一层iframe】")

    def is_alert(self, timeout=3):
        '''判断alert,存在返回alert实例，不存在，返回false'''
        try:
            result = WebDriverWait(self.driver, timeout, 5).until(EC.alert_is_present())
            return result
        except:
            return False

    def assert_alert_info(self, by='xpath', loc='//*[@id="alert"]', expect_value=None):
        try:
            alert = self.find_element(by, loc)
            self.log.info("实际结果：{}".format(alert.text))
            self.log.info("预期结果：{}".format(expect_value))
            assert alert.text.find(expect_value)
        except:
            self.log.info("找不到元素alert!")

    def switch_alert(self):
        '''切换alert'''
        r = self.is_alert()
        if not r:
            self.log.info("alert不存在")
        else:
            return r

    def element_is_visibility(self, by, loc, timeout=10):
        '''显示等待知道元素可见'''
        try:
            ui.WebDriverWait(self.driver, timeout).until(lambda driver: driver.find_element(by, loc).is_displayed())
            self.log.info("【等待元素】时间：{}秒，定位表达式：{}".format(timeout, loc))
            return self.find_element(by, loc)
        except TimeoutError:
            self.log.info("未找到%s" % (loc))
            return False

    def js_slide(self, by, loc):
        '''js滚动浏览器,滚动到指定元素位置'''
        target = self.find_element(by, loc)
        driver.execute_script("arguments[0].scrollIntoView();", target)
        self.log.info("【滚动界面】到:{}  元素".format(loc))

    def js_slide_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        self.log.info("滚动到顶部")

    def js_slide_end(self, x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js)
        self.log.info("滚动到底部")

    def kill_driver(self, driver_name):
        '''结束浏览器进程'''
        if driver_name[-4:].lower() != ".exe":
            driver_name += ".exe"
        os.system("taskkill /f /im " + driver_name)
        self.log.info("【结束浏览器进程】")

    def select_by_index(self, by, loc, index=0):
        '''通过索引,index是索引第几个，从0开始，默认选第一个'''
        ele = self.find_element(by, loc)  # 定位select这一栏
        Select(ele).select_by_index(index)

    def select_by_value(self, by, loc, value):
        '''选择下拉框的某一个值'''
        ele = self.find_element(by, loc)
        Select(ele).select_by_value(value)

    def forward(self):
        '''浏览器前进'''
        self.driver.forward()
        self.log.info("【浏览器前进】")

    def wait(self, wait_time):
        '''等待wait_time,调用time.sleep'''
        time.sleep(wait_time)
        self.log.info('【等待】:' + str(wait_time) + "秒")

    def back(self):
        '''浏览器后退'''
        self.driver.back()
        self.log.info('【浏览器后退】')


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://192.168.2.106:9999/admin/login.html")
    base = Base_Page(driver)
    base.input(By.XPATH, '//*[@id="txtName"]', 'admin')
    base.input(By.XPATH, '//*[@id="txtPwd"]', 'admin')
    base.click(By.XPATH, '//*[@id="fm-login-submit"]')
    time.sleep(5)
    driver.quit()
