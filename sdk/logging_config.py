# logging_config.py

import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_level: str = "INFO", log_file: str = "app.log"):
    """
    Configures the logging settings for the application.
    
    :param log_level: The logging level (default is INFO). Options: DEBUG, INFO, WARNING, ERROR, CRITICAL.
    :param log_file: The log file where logs will be saved (default is app.log).
    """
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(log_level.upper())

    # Create a formatter that will add timestamps to each log entry
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a console handler and set the level to the specified log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.upper())
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Create a file handler that writes logs to a file with rotation
    file_handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=3)
    file_handler.setLevel(log_level.upper())
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Optionally, you could integrate with a log management system (e.g., Logstash, Splunk)
    # For example, use logging.handlers.SysLogHandler() for remote logging

    # If you want to log to an external log management system like Logstash, you can integrate here
    # syslog_handler = logging.handlers.SysLogHandler(address=('localhost', 514))
    # syslog_handler.setFormatter(formatter)
    # logger.addHandler(syslog_handler)

    # Log that logging configuration has been set up
    logger.info("Logging is set up with level %s and log file %s", log_level, log_file)


def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger instance with the given name.
    
    :param name: The name of the logger (typically the module name).
    :return: A logger instance.
    """
    return logging.getLogger(name)
