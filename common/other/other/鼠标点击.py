# -*-coding:utf-8-*-

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
dr.get("http://uat.cbs.bacic5i5j.com/base/")

dr.maximize_window()
time.sleep(3)
# 登录
dr.find_element_by_xpath('//*[@id="username"]').send_keys("695047")
dr.find_element_by_xpath('//*[@id="password"]').send_keys("YAngxiao533")
dr.find_element_by_xpath('//*[@id="btn-submit"]').click()
time.sleep(1)
# 登录楼盘库
dr.find_element_by_xpath('//*[text()="楼盘库"]').click()
# 打开新增楼盘管理新的页面
time.sleep(1)
dr.find_element_by_xpath('//*[@id="side-menu"]/li[5]/ul/li[1]/a').click()

ele2 = dr.find_element_by_xpath('//*[@id="content-main"]/iframe')
dr.switch_to.frame(ele2)

# 点击新增楼盘申请
dr.find_element_by_id("exampleToolbar").click()

# 建筑年代
ele3 = dr.find_element_by_xpath('//*[@id="sel_buildingYear"]')
Select(ele3).select_by_index(3)

# 商圈
dr.find_element_by_xpath('//*[@id="busiId_chosen"]/a/span').click()
time.sleep(1)
dr.find_element_by_xpath('//*[@id="busiId_chosen"]/div/ul/li[2]').click()


time.sleep(1)
# 添加楼盘位置
dr.find_element_by_xpath('//*[@id="baidumarker"]/a/u').click()

ele = dr.find_element_by_xpath('//*[@id="layui-layer-iframe1"]')
dr.switch_to.frame(ele)

kk = dr.find_element_by_xpath('//*[@id="map_edit_container"]')
action = ActionChains(dr)
time.sleep(2)
action.move_by_offset(1028, 385).click(kk).perform()

time.sleep(2)

dr.find_element_by_xpath('//*[@id="confirm"]').click()

js = "window.scrollTo(0,document.body.scrollHeight)"
dr.execute_script(js)

time.sleep(2)
dr.quit()
