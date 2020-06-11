import logging.handlers
import os

BASE_DIR = os.path.dirname(__file__)


def init_log_config():

    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # 创建日志流处理器，用于将日志输出到控制台
    sh = logging.StreamHandler()
    # 创建日志处理器，按时间切割日志，并将日志输出到文件
    fh = logging.handlers.TimedRotatingFileHandler(filename=BASE_DIR+"/log/web自动化演练.log", when="H", encoding="UTF-8", interval=1, backupCount=5)

    # 这是日志的格式
    fmt = "%(asctime)s-%(levelname)s-%(name)s [%(filename)s %(funcName)s-%(lineno)d]:%(message)s"
    # 创建格式化器，并将日志格式参数传入到格式化器，定义日志格式
    formatter = logging.Formatter(fmt=fmt)

    # 将格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
