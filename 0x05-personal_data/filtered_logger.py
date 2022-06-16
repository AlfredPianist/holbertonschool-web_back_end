#!/usr/bin/env python3
"""Filtered logger module. Handles Personal Identifiable Information"""
from typing import List
import re
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Formats a logging record with a set of fields from the
        fields attribute using the filter_datum function.
        Args:
            record: The message record to be formatted.
        Returns:
            The formatted message.
        """
        return filter_datum(self.fields, self.REDACTION,
                            record.getMessage(), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns an obfuscated message given its fields and its redaction.
    Args:
        fields: The fields of the message to be redacted.
        redaction: The redaction of each field's value.
        message: The message to be redacted.
        separator: The separator character between each field.
    Returns:
        The message redacted.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """Gets or creates a logger named 'user_data'. Sets the level to
    INFO, and adds a handler to it with the class RedactingFormatter.
    """
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(stream_handler)
    return logger
