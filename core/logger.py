import os
import sys

from loguru import logger


# ==========================================================
# Create Logs Folder
# ==========================================================

LOG_FOLDER = "logs"

os.makedirs(
    LOG_FOLDER,
    exist_ok=True
)

# ==========================================================
# Remove Default Logger
# ==========================================================

logger.remove()

# ==========================================================
# Console Logger
# ==========================================================

logger.add(

    sys.stdout,

    level="INFO",

    colorize=True,

    enqueue=True,

    backtrace=True,

    diagnose=False,

    format=(
        "<green>{time:HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{message}</cyan>"
    )

)

# ==========================================================
# File Logger
# ==========================================================

logger.add(

    os.path.join(
        LOG_FOLDER,
        "jarvis_{time:YYYY-MM-DD}.log"
    ),

    level="DEBUG",

    rotation="10 MB",

    retention="30 days",

    compression="zip",

    encoding="utf-8",

    enqueue=True,

    backtrace=True,

    diagnose=True,

    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level: <8} | "
        "{module}:{function}:{line} | "
        "{message}"
    )

)


# ==========================================================
# Logger Wrapper
# ==========================================================

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

    @staticmethod
    def exception(message):
        logger.exception(message)