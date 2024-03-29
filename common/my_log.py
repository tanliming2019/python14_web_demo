# _*_ coding:utf-8 _*_
# @time     :  20:52
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : my_logging.py

import logging
from common import project_path
class ReadLogging:

    def my_log(self,level,msg):
        my_logger=logging.getLogger('api_log')
        my_logger.setLevel('DEBUG')


        formatter= logging.Formatter('[%(asctime)s]-[%(levelname)s]-[日志信息]:%(message)s')
        ch=logging.StreamHandler()
        ch.setLevel('INFO')#设置级别
        ch.setFormatter(formatter)#设置格式

        fh=logging.FileHandler(project_path.my_log_path,encoding='utf-8')#写入到指定文件
        fh.setLevel('INFO')#设置级别
        fh.setFormatter(formatter)#设置格式

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(fh)#fh ch
        my_logger.removeHandler(ch)#一定要记得移除掉

    def debug(self,msg):#可以优化的地方
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def error(self,msg):
        self.my_log('ERROR',msg)

if __name__ == '__main__':
    ReadLogging().info('me')
    ReadLogging().info('you')
