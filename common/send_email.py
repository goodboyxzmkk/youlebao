import HTMLReport
import time
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from common import config_manage

# 测试报告路径
report_path = config_manage.REPORT_PATH
email_config = config_manage.get_yaml_config("email.yaml")


def get_newReport():
    '''查找测试报告目录，找到最新生成的测试报告文件'''
    lists = os.listdir(report_path)  # 返回指定路径下的文件和文件夹列表

    '''sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
       最后对lists元素，按文件修改时间大小从小到大排序。'''
    lists.sort(key=lambda fn: os.path.getatime(report_path + "\\" + fn))
    file_new = os.path.join(report_path, lists[-1])  # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    print('最新的测试报告：' + file_new)
    return file_new


def send_Email():
    file_new = get_newReport()
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    # 构造MIMEMultipart对象做为根容器
    msgRoot = MIMEMultipart()
    text_msg = MIMEText(mail_body, 'html', 'utf-8')
    msgRoot.attach(text_msg)
    file_msg = MIMEText(mail_body, 'base64', 'utf-8')
    file_msg["Content-Type"] = 'application/octet-stream'

    # 设置附件头
    basename = os.path.basename(file_new)
    file_msg["Content-Disposition"] = 'attachment; filename=''' + basename + ''
    msgRoot.attach(file_msg)

    # 设置根容器属性
    msgRoot['Subject'] = Header(email_config['邮件标题'], 'utf-8')
    msgRoot['From'] = email_config['发送邮箱']
    msgRoot['To'] = email_config['接收邮箱']  # 发送多个邮件时逗号（,）隔开

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(email_config['邮箱服务器'])
    # smtp.ehlo()
    # smtp.starttls()
    smtp.login(email_config['发送邮箱'], email_config['邮箱授权码'])
    smtp.sendmail(msgRoot['From'], msgRoot['To'].split(','), msgRoot.as_string())
    smtp.quit()
    print('测试报告发送成功！')


if __name__ == '__main__':
    send_Email()
