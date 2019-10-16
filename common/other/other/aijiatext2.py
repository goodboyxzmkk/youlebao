# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

dr = webdriver.Chrome()
dr.get("http://uat.cbs.bacic5i5j.com/base/")
dr.maximize_window()
time.sleep(2)
# 登录
dr.find_element_by_xpath('//*[@id="username"]').send_keys("695047")
dr.find_element_by_xpath('//*[@id="password"]').send_keys("YAngxiao533")
dr.find_element_by_xpath('//*[@id="btn-submit"]').click()
time.sleep(1)
# 楼盘查询
dr.get("http://uat.cbs.bacic5i5j.com/bdir/build/tabs_sel.htm?timestamp=1568273767294")
time.sleep(1)
dr.find_element_by_xpath('//*[@id="buildNameSel"]').send_keys("我的happy")
time.sleep(1)
dr.find_element_by_xpath('//*[@id="btnSearch"]').click()
time.sleep(2)
# //*[@id="dataTable"]/tbody/tr[1]/td[2]/a/u
dr.find_element_by_xpath('//*[@id="dataTable"]/tbody//u').click()
time.sleep(2)
dr.find_element_by_xpath('//*[@id="errorChose"]').click()

time.sleep(5)
frame = dr.find_element_by_xpath('//*[@id="mainframe"]')
dr.switch_to.frame(frame)
# dr.find_element_by_xpath('//*[@id="sprayPropertyName" and @type="text"]').click()
dr.find_element_by_xpath('//*[@id="fileupload1"]').send_keys(r"C:\Users\Ty\Desktop\图片\dd.jpg")

print("执行js")
js = "window.scrollTo(0,document.body.scrollHeight)"
dr.execute_script(js)

time.sleep(3)
dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
time.sleep(2)
dr.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()

#
# dr.find_element_by_xpath('//*[@id="saveBtn"]').click()
# dr.find_element_by_xpath('//*[@id="startSubmit"]').click()
# dr.find_element_by_xpath('//*[@class="layui-layer-btn0"]').click()

# 去处理
# dr.find_element_by_xpath('//*[@data-index="0"]//*[@class="btn btn-outline btn-success btn-xs"]').click()

time.sleep(10)
dr.quit()
