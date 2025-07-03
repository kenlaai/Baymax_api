import datetime
import logging
import os
from tools import constant


class Logs:
    def __init__(self):
        """
        设置日志记录器。
        """
        level = logging.INFO  # 设置日志级别为INFO

        now = datetime.datetime.now()
        formatted_time = now.strftime("%Y%m%d")

        # 创建日志文件夹
        if not os.path.exists(constant.log_dir):
            os.makedirs(constant.log_dir)
        log_file = f'{constant.log_dir}/test_log_{formatted_time}.log'

        # 创建日志记录器
        self.logger = logging.getLogger('Logs')
        self.logger.setLevel(level)

        # 日志格式
        formatter = logging.Formatter('%(asctime)s : %(filename)s - line:%(lineno)d - %(levelname)s -→ %(message)s')

        # 文件处理器
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # 控制台处理器
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)


logs = Logs()