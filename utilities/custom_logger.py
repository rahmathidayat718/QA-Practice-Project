import logging
import os

class Log_Maker:

    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename="reports/logger.log",
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO,
            force=True
        )

        logger = logging.getLogger("CustomLogger")
        logger.setLevel(logging.INFO)
        return logger
