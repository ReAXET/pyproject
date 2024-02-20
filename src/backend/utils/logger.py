"""Custom logger for the application"""
from loguru import logger
import os
import sys
from typing import Any, Dict, List, Tuple
from rich.traceback import install
from rich.logging import RichHandler

# Set up the class BaseLogger

class BaseLogger:
    def __init__(self, log_level: str = "DEBUG") -> None:
        """Initialize the logger with the given log level."""
        self.log_level = log_level
        self.logger = logger
        self.logger.remove()
        self.logger.add(sys.stderr, level=self.log_level)
        self.logger.add(
            os.path.join("logs", "debug.log"),
            level="DEBUG",
            rotation="1 week",
            retention="1 month",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
        self.logger.add(
            os.path.join("logs", "info.log"),
            level="INFO",
            rotation="1 week",
            retention="1 month",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
        self.logger.add(
            os.path.join("logs", "error.log"),
            level="ERROR",
            rotation="1 week",
            retention="1 month",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
        self.logger.add(
            os.path.join("logs", "warning.log"),
            level="WARNING",
            rotation="1 week",
            retention="1 month",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
        self.logger.add(
            os.path.join("logs", "critical.log"),
            level="CRITICAL",
            rotation="1 week",
            retention="1 month",
            enqueue=True,
            backtrace=True,
            diagnose=True,
        )
        install()
        self.logger.enable("backend")

    def log(self, message: str, level: str = "DEBUG") -> None:
        """Log a message at the given level."""
        if level == "DEBUG":
            self.logger.debug(message)
        elif level == "INFO":
            self.logger.info(message)
        elif level == "WARNING":
            self.logger.warning(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "CRITICAL":
            self.logger.critical(message)

    def debug(self, message: str) -> None:
        """Log a message at the DEBUG level."""
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """Log a message at the INFO level."""
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log a message at the WARNING level."""
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log a message at the ERROR level."""
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """Log a message at the CRITICAL level."""
        self.logger.critical(message)

    def exception(self, message: str) -> None:
        """Log an exception at the ERROR level."""
        self.logger.exception(message)

    def success(self, message: str) -> None:
        """Log a message at the SUCCESS level."""
        self.logger.success(message)

    def failure(self, message: str) -> None:
        """Log a message at the FAILURE level."""
        self.logger.failure(message)

    def log_dict(self, data: Dict[str, Any], level: str = "DEBUG") -> None:
        """Log a dictionary at the given level."""
        if level == "DEBUG":
            self.logger.debug(data)
        elif level == "INFO":
            self.logger.info(data)
        elif level == "WARNING":
            self.logger.warning(data)
        elif level == "ERROR":
            self.logger.error(data)
        elif level == "CRITICAL":
            self.logger.critical(data)

    def log_list(self, data: List[Any], level: str = "DEBUG") -> None:
        """Log a list at the given level."""
        if level == "DEBUG":
            self.logger.debug(data)
        elif level == "INFO":
            self.logger.info(data)
        elif level == "WARNING":
            self.logger.warning(data)
        elif level == "ERROR":
            self.logger.error(data)
        elif level == "CRITICAL":
            self.logger.critical(data)

    def log_tuple(self, data: Tuple[Any, ...], level: str = "DEBUG") -> None:
        """Log a tuple at the given level."""
        if level == "DEBUG":
            self.logger.debug(data)
        elif level == "INFO":
            self.logger.info(data)
        elif level == "WARNING":
            self.logger.warning(data)
        elif level == "ERROR":
            self.logger.error(data)
        elif level == "CRITICAL":
            self.logger.critical(data)

    def log_exception(self, message: str, level: str = "ERROR") -> None:
        """Log an exception at the given level."""
        if level == "DEBUG":
            self.logger.debug(message, exc_info=True)
        elif level == "INFO":
            self.logger.info(message, exc_info=True)
        elif level == "WARNING":
            self.logger.warning(message, exc_info=True)
        elif level == "ERROR":
            self.logger.error(message, exc_info=True)
        elif level == "CRITICAL":
            self.logger.critical(message, exc_info=True)

    def log_traceback(self, level: str = "ERROR") -> None:
        """Log the traceback at the given level."""
        if level == "DEBUG":
            self.logger.debug("", exc_info=True)
        elif level == "INFO":
            self.logger.info("", exc_info=True)
        elif level == "WARNING":
            self.logger.warning("", exc_info=True)
        elif level == "ERROR":
            self.logger.error("", exc_info=True)
        elif level == "CRITICAL":
            self.logger.critical("", exc_info=True)

    def log_traceback_message(self, message: str, level: str = "ERROR") -> None:
        """Log the traceback with a message at the given level."""
        if level == "DEBUG":
            self.logger.debug(message, exc_info=True)
        elif level == "INFO":
            self.logger.info(message, exc_info=True)
        elif level == "WARNING":
            self.logger.warning(message, exc_info=True)
        elif level == "ERROR":
            self.logger.error(message, exc_info=True)
        elif level == "CRITICAL":
            self.logger.critical(message, exc_info=True)


# Set up the logger
logger = BaseLogger()

# Create an importable wrapper for the logger
from functools import wraps

def log_wrap(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Exception: {e}")
            return None
    return wrapper
# Q: How will i import the logger in other modules?
# A: You can import the logger like this:
# from backend.utils.logger import logger
# Then you can use it like this:
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
# logger.exception("This is an exception message")
# logger.success("This is a success message")   
# logger.failure("This is a failure message")
# logger.log_dict({"key": "value"}, level="DEBUG")
# logger.log_list(["item1", "item2"], level="INFO")
# logger.log_tuple(("item1", "item2"), level="WARNING")
# logger.log_exception("This is an exception message", level="ERROR")
# logger.log_traceback(level="CRITICAL")
# logger.log_traceback_message("This is a traceback message", level="DEBUG")
# You can also log at a specific level like this:
# logger.log("This is a debug message", level="DEBUG")
# logger.log("This is an info message", level="INFO")
# logger.log("This is a warning message", level="WARNING")
# logger.log("This is an error message", level="ERROR")
# logger.log("This is a critical message", level="CRITICAL")
# You can also log a dictionary, list, or tuple like this:
# logger.log_dict({"key": "value"}, level="DEBUG")
# logger.log_list(["item1", "item2"], level="INFO")
# logger.log_tuple(("item1", "item2"), level="WARNING")
# You can also log an exception like this:
# logger.log_exception("This is an exception message", level="ERROR")
# You can also log the traceback like this:
# logger.log_traceback(level="CRITICAL")
# You can also log the traceback with a message like this:
# logger.log_traceback_message("This is a traceback message", level="DEBUG")
