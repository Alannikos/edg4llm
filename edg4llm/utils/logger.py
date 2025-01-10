import datetime
import logging

__all__ = ['custom_logger']

# Define log level colors for terminal output
LOG_COLORS = {
    'DEBUG': '\033[96m',  # Cyan
    'INFO': '\033[92m',   # Green
    'WARNING': '\033[93m',  # Yellow
    'ERROR': '\033[91m',    # Red
    'CRITICAL': '\033[1;91m',  # Bold Red
    'RESET': '\033[0m',  # Reset color
}

def custom_logger(name: str):
    """
    Creates a custom logger with color-coded log levels and UTC+8 time formatting.

    Parameters
    ----------
    name : str
        The name of the logger, typically the name of the module or application.

    Returns
    -------
    logging.Logger
        A customized logger instance with color-coded levels and UTC+8 timezone support.

    Notes
    -----
    - Log levels are color-coded for easier readability in terminal output.
    - Log messages use UTC+8 timezone formatting.
    - The logger prevents propagation to root loggers and clears existing handlers.
    - The logger uses a custom `StreamHandler` with color support.
    """
    # Create a logger instance
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)  # Default log level
    logger.propagate = False  # Disable propagation to root loggers
    logger.handlers = []  # Clear any existing handlers

    # Define a custom log message format
    formatter = logging.Formatter(
        '[%(asctime)s]-[%(name)s:%(levelname)s]:%(message)s'
    )

    # Custom time converter to use UTC+8
    def _utc8_aera(timestamp):
        """
        Convert a timestamp to a UTC+8 time tuple.

        Parameters
        ----------
        timestamp : float
            The timestamp to convert.

        Returns
        -------
        time.struct_time
            A time tuple in UTC+8 timezone.
        """
        now = datetime.datetime.fromtimestamp(timestamp, tz=datetime.timezone.utc) + datetime.timedelta(hours=8)
        return now.timetuple()

    # Set the custom time converter in the formatter
    formatter.converter = _utc8_aera

    # Define a custom StreamHandler with color-coded log levels
    class ColorStreamHandler(logging.StreamHandler):
        """
        A custom logging stream handler that adds color coding to log messages.

        Methods
        -------
        emit(record):
            Formats and outputs a log record with color coding based on log level.
        """
        def emit(self, record):
            """
            Format and emit a log record with color coding.

            Parameters
            ----------
            record : logging.LogRecord
                The log record to process and output.
            """
            try:
                msg = self.format(record)  # Format the log record
                color = LOG_COLORS.get(record.levelname, LOG_COLORS['RESET'])  # Get the color for the log level
                # Write the log message with color
                self.stream.write(f"{color}{msg}{LOG_COLORS['RESET']}\n")
                self.flush()  # Flush the stream
            except Exception:
                self.handleError(record)  # Handle any errors during logging

    # Create and configure the custom handler
    custom_handler = ColorStreamHandler()
    custom_handler.setFormatter(formatter)

    # Add the custom handler to the logger
    logger.addHandler(custom_handler)

    return logger
