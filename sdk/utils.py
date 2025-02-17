# utils.py

import re
from typing import Any

def validate_email(email: str) -> bool:
    """
    Validates if the provided email address is in the correct format.
    
    :param email: Email string to be validated.
    :return: True if valid, False otherwise.
    """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.match(email_regex, email))


def validate_token_format(token: str) -> bool:
    """
    Validates if the provided token is in a valid format.
    
    :param token: Token string to be validated.
    :return: True if valid, False otherwise.
    """
    token_regex = r"^\$SUDO-[A-Za-z0-9]+$"
    return bool(re.match(token_regex, token))


def convert_to_camel_case(s: str) -> str:
    """
    Converts a string from snake_case to camelCase.
    
    :param s: Input string in snake_case format.
    :return: String in camelCase format.
    """
    words = s.split('_')
    return words[0] + ''.join(word.title() for word in words[1:])


def convert_to_snake_case(s: str) -> str:
    """
    Converts a string from camelCase to snake_case.
    
    :param s: Input string in camelCase format.
    :return: String in snake_case format.
    """
    return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', s).lower()


def deep_copy(obj: Any) -> Any:
    """
    Performs a deep copy of an object (e.g., list, dict).
    
    :param obj: Object to be deep-copied.
    :return: A new object that is a deep copy of the original.
    """
    from copy import deepcopy
    return deepcopy(obj)


def is_valid_ip(ip: str) -> bool:
    """
    Checks if the given string is a valid IP address.
    
    :param ip: String to be checked for IP address format.
    :return: True if valid, False otherwise.
    """
    ip_regex = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return bool(re.match(ip_regex, ip))


def safe_get(dictionary: dict, key: str, default: Any = None) -> Any:
    """
    Safely retrieves a value from a dictionary, returning a default value if the key is not found.
    
    :param dictionary: The dictionary from which the value is retrieved.
    :param key: The key to look up.
    :param default: The default value to return if the key is not found (default is None).
    :return: The value associated with the key, or the default value.
    """
    return dictionary.get(key, default)


def format_logs(message: str, level: str = "INFO") -> str:
    """
    Formats log messages for consistent logging.
    
    :param message: The message to log.
    :param level: The log level (e.g., INFO, ERROR).
    :return: The formatted log string.
    """
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {level}: {message}"


def get_env_var(variable_name: str) -> str:
    """
    Retrieves the value of an environment variable, with an exception if not found.
    
    :param variable_name: The name of the environment variable.
    :return: The value of the environment variable.
    :raises ValueError: If the environment variable is not found.
    """
    import os
    value = os.getenv(variable_name)
    if value is None:
        raise ValueError(f"Environment variable {variable_name} is not set.")
    return value
