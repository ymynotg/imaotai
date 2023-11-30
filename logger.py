import logging
import time
import datetime
def log():
    #创建logger，参数为指定的logger名字,如果参数为空则返回root logger
    logger = logging.getLogger("GaoAddLogger")
    logger.setLevel(logging.DEBUG) #设置logger日志等级
    #这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not  logger.handlers:
        #创建handler
        fh = logging.FileHandler(f'{ datetime.date.today().strftime("%Y%m%d")}.log',encoding="utf-8")
        ch = logging.StreamHandler()
        
        fh.setLevel(logging.DEBUG)
        ch.setLevel(logging.INFO)

        #设置输出日志格式
        formatter = logging.Formatter(
            fmt="%(asctime)s %(name)s %(filename)s : %(levelname)s %(message)s",
            datefmt="%Y/%m/%d %X"
            )
        #为handler指定输出格式
        fh.setFormatter(formatter)
        #ch.setFormatter(formatter)
    

        #为logger添加的日志处理器
        logger.addHandler(fh)
        logger.addHandler(ch)
    return logger #直接返回logger





'''
import datetime
import logging

#格式化文件名称
fileFormat = datetime.date.today().strftime("%Y%m%d")

#创建logger
logger = logging.getLogger("GaoAddlogger")

#
logger.setLevel(logging.DEBUG)


ch = logging.StreamHandler( )
fh = logging.FileHandler(f'{fileFormat}.log')

#format= logging.Formatter(fmt='%(asctime")s %(filemame)s %(levelname)s %(message)s',datefmt="%Y%m%d %x")
formatter = logging.Formatter(fmt="%(asctime)s %(filemame)s %(levelname)s  %(message)s",datefmt="%Y/%m/%d %X")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

ch.setLevel(logging.WARNING)
fh.setLevel(logging.DEBUG)


logger.addHandler(ch)
logger.addHandler(fh)
logger.warning("泰拳警告")
logger.error("aaa")
#logger.info("the first time"')
'''


