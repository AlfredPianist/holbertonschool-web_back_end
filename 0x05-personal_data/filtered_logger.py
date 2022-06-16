#!/usr/bin/env python3
"""Filtered logger module. Handles Personal Identifiable Information"""
from typing import List
import re
import logging
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.__fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Formats a logging record with a set of fields from the
        fields attribute using the filter_datum function.
        Args:
            record: The message record to be formatted.
        Returns:
            The formatted message.
        """
        message = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.__fields, self.REDACTION,
                            message, self.SEPARATOR)


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
    Return:
        The logger.
    """
    logger: logging.Logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler: logging.StreamHandler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a mysql connection"""
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"))


def main():
    """Main entrypoint"""
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    column_names = [column[0] for column in cursor.description]
    log = get_logger()

    for record in cursor:
        message = ''.join(f'{column}={value}{RedactingFormatter.SEPARATOR} '
                          for column, value in zip(column_names, record))
        log.info(message)

    cursor.close()
    database.close()


if __name__ == "__main__":
    main()
