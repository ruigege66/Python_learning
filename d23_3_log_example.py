
#现在有一下几个日志记录的需求：
#（1）要求将所有级别的所有日志写入磁盘文件
#（2）all.log文件中记录所有的日志信息，日志格式为：日期和时间-日志级别-日志信息
#（3）error.log文件中单独记录error及以上级别的日志信息，日志格式：日期和时间-日志级别-文件名【：行号】- 日志信息
#（4）要求all.log在每天凌晨进行日志切割

#分析
#(1)要记录所有级别的日志，因此日志器的有效level需要设置为最低级别  --DEBUG
#(2)日志需要被发送到两个不同的目的地，因此需要为日志设置两个handler；另外。两个目的地都是磁盘文件。因此这两个handler都是与fileHander
#(3)all.log要求按照时间进行日志切割，因此它需要logging.handler.TimeRotatingFileHandler；而error.log没有要求日志切割。因此
#(4)两个日志文件的格式不同,因此需要对两个handler分别进行设置格式器

import logger
import logging.handlers
import datetime


#定义Logger
logger = logging.getLogger("mylogger")
logging.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler("all.log",when="midnight",interval=1,backupCount=7,atTime=None)
rf_handler.setFormatter(logging.Formatter("%(asctime)s-%(levelname)s-%(message)s"))

f_handler = logging.FileHandler("error.log")
f_handler = setLevel(logging.ERROR)
f_handler.setFormat(logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s[:%(lineno)d-%(message)s)")

#把相应的处理器组装到logger上
logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
