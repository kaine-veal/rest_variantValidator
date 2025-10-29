import logging
import sys

# Create a logger instance
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)  # Set logger level to WARNING

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Create a handler for stdout (Error messages)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.ERROR)  # Log error and critical messages to stdout
stdout_handler.setFormatter(formatter)

# Create a handler for stderr (Error and Critical messages)
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.ERROR)  # Log error and critical messages to stderr
stderr_handler.setFormatter(formatter)

# Create a file handler (all levels)
file_handler = logging.FileHandler("rest_api.log")  # Log all levels to a file
file_handler.setLevel(logging.DEBUG)  # Log warning and above to file
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)
logger.addHandler(file_handler)