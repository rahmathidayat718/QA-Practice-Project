import logging
import os

class Log_Maker:
    def __init__(self, log_file="logs/bnext.log"):
        os.makedirs("logs", exist_ok=True)  # Membuat folder logs jika belum ada
        self.logger = logging.getLogger("CustomLogger")
        self.logger.setLevel(logging.DEBUG)

        # File Handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        # Tambahkan handler ke logger
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)

    def info(self, message):
        self.logger.info(message)

    def pass_log(self, message):
        self.logger.info(f"PASS - {message}")

    def fail(self, message):
        self.logger.error(f"FAIL - {message}")
