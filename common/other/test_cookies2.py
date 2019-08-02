import json
import time
import pickle

from selenium import webdriver
import unittest


class Login(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://localhost:9999/admin")
        driver.find_element_by_xpath('//*[@id="txtName"]').send_keys("admin")
        driver.find_element_by_xpath('//*[@id="txtPwd"]').send_keys("admin")
        driver.find_element_by_xpath('//*[@id="fm-login-submit"]').click()
        dictCookies = driver.get_cookies()
        print(dictCookies)
        pickle.dump(dictCookies, open("cookies.pkl", "wb"))

        driver.get("http://localhost:9999/admin")
        driver.delete_all_cookies()
        print("删除cookies后:{}".format(driver.get_cookies()))
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            cookie_dict = {
                "domain": ".localhost",  # 火狐浏览器不用填写，谷歌要需要
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            driver.add_cookie(cookie_dict)
        print(driver.get_cookies())
        driver.get('http://localhost:9999/admin/Container.html')


if __name__ == '__main__':
    unittest.main()
