from edg4llm.utils.logger import custom_logger

logger = custom_logger('test', 'DEBUG')

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
