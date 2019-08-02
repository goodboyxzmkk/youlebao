# coding:utf-8
import yaml, json
import os

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."))  # 项目路径
REPORT_PATH = os.path.join(PROJECT_PATH, "test_report\\report\\")  # 测试报告目录
SCREEN_PATH = os.path.join(PROJECT_PATH, "test_report\\screen\\")  # 错误截图目录
LOG_PATH = os.path.join(PROJECT_PATH, "test_report\\logs\\")  # 日志目录
TESTCASE_PATH = os.path.join(PROJECT_PATH, "test_case\\")  # 测试用例目录
TESTDATA_PATH = os.path.join(PROJECT_PATH, "test_data\\")  # 测试数据目录
ELEMENT_PATH = os.path.join(PROJECT_PATH, "po\\page_loc\\")  # 页面元素定位目录
CONIFGS_PATH = os.path.join(PROJECT_PATH, "configs\\")  # 配置文件目录


def get_yaml_config(file_name='configs.yaml'):
    configpath = os.path.join(PROJECT_PATH, "configs")
    yamlPath = os.path.join(configpath, file_name)  # configName.yaml文件
    f = open(yamlPath, 'r', encoding='UTF-8')
    cfg = f.read()  # 读出来是字符串
    dic = yaml.load(cfg, Loader=yaml.FullLoader)  # 用load方法转字典
    return dic


def get_yaml_page_loc(page_name):
    yamlPath = os.path.join(ELEMENT_PATH, page_name)  # 获取page元素定位目录
    f = open(yamlPath, 'r', encoding='UTF-8', errors='ignore')
    dic = yaml.load(f, Loader=yaml.FullLoader)  # 用load方法转字典
    return dic


def write_cookies(cookies):
    COOKIES_PATH = CONIFGS_PATH + 'cookies.json'
    with open(COOKIES_PATH, 'w') as fp:
        fp.write(json.dumps(cookies))
        fp.close()


def read_cookies():
    COOKIES_PATH = CONIFGS_PATH + 'cookies.json'
    with open(COOKIES_PATH) as fp:
        cookies = json.load(fp)
        fp.close()
        return cookies


if __name__ == "__main__":
    loginpage = get_yaml_page_loc('login_loc.yaml')
    print("URL:" + str(loginpage['URL_TEST']))
