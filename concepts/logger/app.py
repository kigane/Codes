import sys
import logging
import logging.handlers
from time import sleep

"""
    basicConfig用于设置root logger,且以第一次设置的为准,所以如果引入的其他
    模块也使用了root logger,则只会使用第一个引入的模块的设置。
    asctime: 时间戳
    levelname: 消息等级
    module: py文件名/模块名
    name: logger的名字
"""
import basic
logging.basicConfig(filename='app1.log', 
                    level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] in %(module)s: %(message)s')

# 特定模块的logger基本使用方法
# handler可以同时设置多个
logger = logging.Logger(__name__)

file_handler = logging.FileHandler('app.log')
stream_handler = logging.StreamHandler(stream=sys.stdout)
rotate_file_handler = logging.handlers.RotatingFileHandler(
                        'app_rot.log', 
                        maxBytes=100, # 日志文件最大大小
                        backupCount=5) # 最多保存的日志文件个数
time_file_handler = logging.handlers.TimedRotatingFileHandler(
                        'app_time.log',
                        when='s', # S,M,H,D,W0-W6,midnight
                        interval=1, # 时间间隔=interval*when
                        backupCount=5)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] in %(module)s: %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
rotate_file_handler.setFormatter(formatter)
time_file_handler.setFormatter(formatter)

logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
# logger.addHandler(rotate_file_handler)
# logger.addHandler(time_file_handler)


if __name__ == "__main__":
    for i in range(5):
        logger.info(f'Hello Logger {i}')
        sleep(1)
        logging.info('Ehlo')