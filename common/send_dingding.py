'''封装钉钉群发消息'''
import requests, json


def send_ding(message):
    url = "https://oapi.dingtalk.com/robot/send?access_token=3c3a9adb21ff20468a69b9c3f4c5dee8295b26215ea9992740a8116d845d8e00"
    String_textMsg = {
        "msgtype": "text",
        "text": {
            "content": message
        },
        "at": {
            "atMobiles": [
                "18620101998"  # 如果需要@某人，这里写他的手机号 与at 所有人不可同时用
            ],
            # "isAtAll": 1  # 如果需要@所有人，这些写1
        }
    }
    headers = {
        'Content-Type': 'application/json ;charset=utf-8'
    }
    f = requests.post(url, data=json.dumps(String_textMsg), headers=headers)
    if f.status_code == 200:
        return True
    else:
        return False


def send_ding_to_url(message, file_url):
    url = "https://oapi.dingtalk.com/robot/send?access_token=3c3a9adb21ff20468a69b9c3f4c5dee8295b26215ea9992740a8116d845d8e00"
    String_textMsg = {
        "msgtype": "markdown",
        "markdown": {
            "title": message,
            "text": file_url
        },
        "at": {
            "atMobiles": [
                "18620101998"  # 如果需要@某人，这里写他的手机号
            ],
            "isAtAll": 1  # 如果需要@所有人，这些写1
        }
    }
    headers = {
        'Content-Type': 'application/json ;charset=utf-8'
    }
    f = requests.post(url, data=json.dumps(String_textMsg), headers=headers)
    if f.status_code == 200:
        return True
    else:
        return False

if __name__ == '__main__':
    send_ding("这个可以有")
