import logging
import os
from dotenv import load_dotenv

load_dotenv()

class Logger:
    """
        Custom Logger wrapper around Python's built-in logging module.
        Ensures a single logger instance is reused across the project.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            cls._instance.__init()


    def __init__(self):
        log_level_str = os.getenv("LOG_LEVEL" , "DEBUG").upper()
        log_level = getattr(logging , log_level_str , logging.DEBUG)
        self._logger = logging.getLogger("automation")
        self._logger.setLevel(log_level)

        if not self._logger.handlers:  # avoid adding handlers twice

            #console handler
            stream_handler = logging.StreamHandler()

            #file handler
            log_file = os.getenv("LOG_FILE", "automation.log")
            file_handler = logging.FileHandler(log_file)


            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            stream_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)



    def get_logger(self):
        return self._logger


