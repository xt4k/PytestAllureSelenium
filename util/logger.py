import logging

class Logger:

    @staticmethod
    def get_shared_logger(prefix, log_level):
        logger = logging.getLogger("SharedLogger")

        if not logger.handlers:
            file_handler = logging.FileHandler("../shared_log_tests.log")
            formatter = logging.Formatter(f"%(asctime)s:{prefix} : %(levelname)s : %(name)s : %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(log_level)

        return logger
