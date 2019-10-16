from selenium import webdriver
import os,time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.1.147:9999/admin")
driver.find_element_by_xpath('//*[@id="txtName"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="txtPwd"]').send_keys('admin')
driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mumu_group100003800"]').click()
ele= driver.find_element_by_xpath("//*[contains(@src,'Game/ProfessionalGameHome.html')]")
driver.switch_to.frame(ele)
driver.find_element_by_xpath('//*[@id="menu_100003800"]').click()
time.sleep(3)
driver.switch_to.default_content()
ele2= driver.find_element_by_xpath("//*[contains(@src,'Goods/ProfessionalGoodsList.html')]")
driver.switch_to.frame(ele2)

driver.find_element_by_xpath('//*[contains(text(),"批量操作")]').click()
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(),'导入商品') and @class='el-dropdown-menu__item']").click()
# driver.find_element_by_xpath('//*[@id="File0"]').click()
driver.find_element_by_xpath('//*[@id="File0"]').send_keys(r"E:\测试任务\AutoTest\AutoItUpFile.exe")

# os.system(r"E:\测试任务\AutoTest\AutoItUpFile.exe")
