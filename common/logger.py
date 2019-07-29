# _*_ coding: utf-8 _*_
import logging, os, time
from common import config_manage


class Logger():
    def __init__(self):
        '''指定保存日志的文件路径，日志级别，以及调用文件，将日志存入到指定的文件中'''
        # 文件名
        self.logName = os.path.join(config_manage.LOG_PATH, '%s.log' % time.strftime('%Y-%m-%d'))
        # 创建logger
        self.logger = logging.getLogger('YCH')
        # 设置日志等级
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')

    def __console(self, level, message):
        # 创建一个filehandler,用于写日志到本地
        fh = logging.FileHandler(self.logName, 'a')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)

        # 级logger 添加hander
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level.lower() == 'info':
            self.logger.info(message)
        if level.lower() == 'debug':
            self.logger.debug(message)
        if level.lower() == 'warning':
            self.logger.warning(message)
        if level.lower() == 'error':
            self.logger.error(message)

        # 避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)

    def debug(self, msg):
        self.__console('debug', msg)

    def info(self, msg):
        self.__console('info', msg)

    def warning(self, msg):
        self.__console('warning', msg)

    def error(self, msg):
        self.__console('error', msg)


if __name__ == '__main__':
    log = Logger()
    log.debug("This is debug")
    log.info("This is info")
    log.warning("This is warning")
    log.error("This is error")
