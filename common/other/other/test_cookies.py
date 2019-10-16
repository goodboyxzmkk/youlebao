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
        jsonCookies = json.dumps(dictCookies)
        print(jsonCookies)
        pickle.dump(dictCookies, open("cookies.pkl", "wb"))
        with open('cookies.json', 'w') as f:
            f.write(jsonCookies)
        time.sleep(2)
        driver.get("http://localhost:9999/admin")
        time.sleep(2)
        driver.delete_all_cookies()
        print("删除cookies后:{}".format(driver.get_cookies()))

        with open('cookies.json', 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        for cookies in listCookies:
            print(type(cookies))
            driver.add_cookie(cookies)
        time.sleep(2)
        print(driver.get_cookies())
        driver.get('http://localhost:9999/admin/Container.html')

        time.sleep(2)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
