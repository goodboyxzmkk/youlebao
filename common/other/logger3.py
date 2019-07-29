# _*_ coding: utf-8 _*_
import logging
import os.path
import time
from common import config_manage
from logging.handlers import TimedRotatingFileHandler

log_config = config_manage.get_yaml_config('logger_config.yaml')
log_path = config_manage.LOG_PATH  # 在该路径下新建下级目录


class Logger(object):
    def __init__(self):
        self.logger = logging.getLogger(log_config['日志名称'])
        logging.root.setLevel(logging.NOTSET)

        self.backup_count = log_config['保留日志天数']

        # 日志输出级别
        self.console_output_level = log_config['控制台日志级别']
        self.file_output_level = log_config['文件日志级别']
        # 日志输出格式
        self.formatter = logging.Formatter(log_config['日志格式'])

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        log_name = time.strftime('%Y-%m-%d.log', time.localtime(time.time()))  # 返回当前时间的年月日作为目录名称
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(
                filename=os.path.join(log_path, log_name),
                when='D',
                interval=1,
                backupCount=int(self.backup_count),
                delay=True,
                encoding='utf-8'
            )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
            # file_list = os.listdir(log_path)
            #
            # file_path = os.path.join(log_path, file_list[0])
            # if len(file_list) > 10:
            #     os.remove(file_path)
        return self.logger


log = Logger().get_logger()
