import datetime
import logging

__all__ = ['custom_logger']

# 定义不同日志级别的颜色
LOG_COLORS = {
    'DEBUG': '\033[96m',  # 青色
    'INFO': '\033[92m',   # 绿色
    'WARNING': '\033[93m',  # 黄色
    'ERROR': '\033[91m',    # 红色
    'CRITICAL': '\033[1;91m',  # 粗体红色
    'RESET': '\033[0m',  # 重置颜色
}

def custom_logger(name: str, log_level: str):
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False
    logger.handlers = []

    # 自定义log 格式
    formatter = logging.Formatter(
        '[%(asctime)s]-[%(name)s:%(levelname)s]-[%(process)d-%(thread)d]:%(message)s'
    )

    # 使用utc-时间
    def _utc8_aera(timestamp):
        now = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc)+ datetime.timedelta(hours=8)
        return now.timetuple()

    formatter.converter = _utc8_aera

    # 自定义的StreamHandler，添加颜色支持
    class ColorStreamHandler(logging.StreamHandler):
        def emit(self, record):
            try:
                msg = self.format(record)
                color = LOG_COLORS.get(record.levelname, LOG_COLORS['RESET'])
                # 为日志内容加上颜色
                self.stream.write(f"{color}{msg}{LOG_COLORS['RESET']}\n")
                self.flush()
            except Exception:
                self.handleError(record)

    custom_handler = ColorStreamHandler()
    custom_handler.setFormatter(formatter)

    logger.addHandler(custom_handler)

    return logger
