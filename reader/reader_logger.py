import logging
from . import DATA_DIR


def write_logs(text: str, level_type="info"):
    logger = logging
    logger_format = "%(levelname)s %(asctime)s: %(message)s"
    logger.basicConfig(filename=DATA_DIR + "/reader_logs.log",
                       filemode="w",
                       level=logging.INFO,
                       format=logger_format,
                       datefmt='%Y:%m:%d %H:%M:%S')
    if level_type == "info":
        logger.info(text)
    elif level_type == "error":
        logger.error(text)
    elif level_type == "warning":
        logger.warning(text)
