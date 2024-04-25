import logging

"""
在日志中，通常会使用不同的级别来表示不同的日志消息的重要性和严重程度。常见的日志级别包括：INFO、WARNING、ERROR等。

INFO级别：INFO级别的日志用于记录一些普通的信息消息，用于提供程序的运行状态、进展情况等。这些日志消息通常是一些正常的操作、事件或状态的记录，不会影响程序的正常运行。

WARNING级别：WARNING级别的日志用于记录一些警告信息，表示程序可能会遇到一些潜在的问题或异常情况，但不会导致程序的中断或错误。这些日志消息通常用于提醒开发者或管理员注意某些可能需要关注或处理的情况。

ERROR级别：ERROR级别的日志用于记录一些错误信息，表示程序遇到了一些无法继续执行的错误或异常情况。这些日志消息通常用于指示程序发生了一些严重的问题，需要进行错误处理或修复。

总结来说，INFO级别的日志用于提供程序的运行状态和进展情况，WARNING级别的日志用于提醒潜在的问题或异常情况，ERROR级别的日志用于指示严重的错误或异常情况。根据具体的需求和情况，可以选择适当的日志级别来记录相应的日志消息。
"""
class MyLogger:
    def __init__(self, log_file, log_level=logging.INFO):
        self.log_file = log_file
        self.log_level = log_level
        self.logger = self._create_logger()

    def _create_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(self.log_level)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(self.log_level)
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger

    def log(self, message, level=logging.INFO):
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)
    def loging_info(self):
        logger.log(logging.INFO)
    def loging_warning(self):
        logger.log(logging.WARNING)
    def loging_error(self):
        logger.log(logging.ERROR)

# 使用示例
logger = MyLogger('mylog.log')

logger.log('This is an info message', logging.INFO)
logger.log('This is a warning message', logging.WARNING)
logger.log('This is an error message', logging.ERROR)
