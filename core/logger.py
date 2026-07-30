from loguru import logger
import os
import sys

# Create logs folder if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Remove default logger
logger.remove()

# Console logging
logger.add(
    sys.stdout,
    format="<green>{time:HH:mm:ss}</green> | <level>{level}</level> | <cyan>{message}</cyan>",
    level="INFO",
    colorize=True
)

# File logging
logger.add(
    os.path.join(LOG_DIR, "jarvis.log"),
    rotation="5 MB",
    retention="10 days",
    compression="zip",
    level="DEBUG",
    encoding="utf-8"
)


class JarvisLogger:

    @staticmethod
    def info(message):
        logger.info(message)

    @staticmethod
    def success(message):
        logger.success(message)

    @staticmethod
    def warning(message):
        logger.warning(message)

    @staticmethod
    def error(message):
        logger.error(message)

    @staticmethod
    def debug(message):
        logger.debug(message)

    @staticmethod
    def critical(message):
        logger.critical(message)