# coding:utf-8
from selenium import webdriver


class Driver_Manager():
    def get_driver(self, type):
        if type.lower() == 'firefox':
            self.driver = webdriver.Firefox()
            self.driver.maximize_window()
            return self.driver
        elif type.lower() == 'ie':
            self.driver = webdriver.Ie()
            self.driver.maximize_window()
            return self.driver
        elif type.lower() == 'h5':  # H5页面
            mobile_emulation = {'deviceName': 'iPhone 6/7/8'}
            options = webdriver.ChromeOptions()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
            return self.driver
        else:  # chrome
            # option = webdriver.ChromeOptions()
            # option.add_argument('headless')  # 静默模式
            # self.driver = webdriver.Chrome(
            #     "C:\\Users\\Ty\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe", chrome_options=option)
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            return self.driver
