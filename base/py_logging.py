import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("FLogger")

# Loggers    expose the interface that application code directly uses.
# Handlers   send the log records(created by loggers) to the appropriate destination.
# Filters    provide a finer grained facility for determining which log records to output.
# Formatters specify the layout of log records in the final output.

# root logger
# logging.basicConfig( # filename='./example.log', encoding='utf-8',
#     format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s: %(message)s', datefmt='%Y/%m/%d %H:%M:%S',
#     level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('%s before you %s', 'Look', 'leap!')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

# __name__的值在执行的py文件中为'__main__'，在导入的文件中为 package.module 形式。
# 另外，python的logger的实例由其名字区分，且有继承关系, 如foo是foo.bar, foo.ku.a的父级。默认子级的messages会传播到父级的handler。故，父级定义好handler后，子代可以直接用。

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('%s before you %s', 'Look', 'leap!')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')

for i in range(170):
    logger.info('content exceeded?')

logger.error('Hello')
