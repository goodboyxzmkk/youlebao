# _*_ coding: utf-8 _*_
import logging
import os.path
import time
from common import config_manage


class Logger(object):
    def __init__(self):
        '''指定保存日志的文件路径，日志级别，以及调用文件，将日志存入到指定的文件中'''
        current_time = time.strftime('%Y%m%d%H%M',
                                     time.localtime(time.time()))  # 返回当前时间
        new_name = config_manage.LOG_PATH  # 在该路径下新建下级目录
        dir_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 返回当前时间的年月日作为目录名称
        isExists = os.path.exists(new_name + dir_time)  # 判断该目录是否存在
        '''
        if not isExists:
            os.makedirs(new_name + dir_time)
            print(new_name + dir_time + "log目录创建成功")

        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(new_name + "log目录： %s 已存在" % dir_time)
            '''
        try:
            # 创建一个logger(初始化logger)
            self.log = logging.getLogger("YCH")
            self.log.setLevel(logging.INFO)

            # 创建一个handler，用于写入日志文件
            log_name = new_name + dir_time + '.log'  # 定义日志文件的路径以及名称

            self.fh = logging.FileHandler(log_name)
            self.fh.setLevel(logging.INFO)

            # 再创建一个handler，用于输出到控制台
            self.ch = logging.StreamHandler()
            self.ch.setLevel(logging.INFO)

            # 定义handler的输出格式
            formatter = logging.Formatter('[%(asctime)s] - %(name)s - %(levelname)s - %(message)s')
            self.fh.setFormatter(formatter)
            self.ch.setFormatter(formatter)

            # 给logger添加handler
            self.log.addHandler(self.fh)
            self.log.addHandler(self.ch)
        except Exception as e:
            print("输出日志失败！ %s" % e)

    # 日志接口，用户只需调用这里的接口即可，这里只定位了INFO, WARNING, ERROR三个级别的日志，可根据需要定义更多接口

    def info(cls, msg):
        cls.log.info(msg)
        return

    def warning(cls, msg):
        cls.log.warning(msg)
        return

    def error(cls, msg):
        cls.log.error(msg)
        return

    def del_handler(cls):
        #  在记录日志之后移除句柄
        cls.log.removeHandler(cls.ch)
        cls.log.removeHandler(cls.fh)


if __name__ == '__main__':
    logger = Logger()
    logger.info('This is info')
    logger.warning('This is warning')
    logger.error('This is error')
