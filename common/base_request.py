import requests
import json


class Base_Request():
    def __init__(self, session):
        self.session = session

    def send_post(self, url, data, header=None, cookies=None):
        if header != None:
            res = self.session.post(url=url, data=data, headers=header, cookies=cookies)
        else:
            res = self.session.post(url=url, data=data, cookies=cookies)
        return res.json()

    def send_get(self, url, data=None, header=None, cookies=None):
        if header != None:
            res = self.session.get(url=url, data=data, headers=header, cookies=cookies, verify=False)
        else:
            res = self.session.get(url=url, data=data, cookies=cookies, verify=False)
        return res.json()

    def send_request(self, method, url, data=None, header=None, cookies=None):
        if method.lower() == 'post':
            res = self.send_post(url, data, header, cookies)
        else:
            res = self.send_get(url, data, header, cookies)
        return json.dumps(res, ensure_ascii=False)
