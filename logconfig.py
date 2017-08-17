import logging
import os, sys


def getlogger(loggername):
    # 1、创建一个logger
    logger = logging.getLogger(loggername)
    logger.setLevel(logging.DEBUG)
    # log_file = os.path.join(os.getcwd(),'logfile.log')
    # if not os.path.exists(log_file):
    # f = open(log_file, 'w')
    # logging.basicConfig(filename=log_file,filemode='w')

    # 2、创建一个handler，用于写入日志文件
    filehandler = logging.FileHandler('test.log')
    filehandler.setLevel(logging.DEBUG)

    # 再创建一个handler，用于输出到控制台
    consolehandler = logging.StreamHandler()
    consolehandler.setLevel(logging.DEBUG)

    # 3、定义handler的输出格式（formatter）
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 4、给handler添加formatter
    filehandler.setFormatter(formatter)
    consolehandler.setFormatter(formatter)

    # 5、给logger添加handler
    logger.addHandler(filehandler)
    logger.addHandler(consolehandler)
    return logger
