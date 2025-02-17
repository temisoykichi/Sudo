# errors.py

class BaseError(Exception):
    """
    The base class for all custom exceptions in the project.
    """
    def __init__(self, message: str, *args):
        super().__init__(message, *args)
        self.message = message

    def __str__(self):
        return f"Error: {self.message}"


class PolicyViolationError(BaseError):
    """
    Raised when a security policy is violated (e.g., an unauthorized command is requested).
    """
    def __init__(self, policy_name: str, *args):
        self.policy_name = policy_name
        message = f"Policy '{policy_name}' violation occurred."
        super().__init__(message, *args)

    def __str__(self):
        return f"PolicyViolationError: {self.message}"


class ContainerError(BaseError):
    """
    Raised when there is an issue with container management (e.g., failure to create or execute a container).
    """
    def __init__(self, container_id: str, error_details: str, *args):
        self.container_id = container_id
        self.error_details = error_details
        message = f"Error with container '{container_id}': {error_details}"
        super().__init__(message, *args)

    def __str__(self):
        return f"ContainerError: {self.message}"


class BlockchainError(BaseError):
    """
    Raised when an issue occurs with blockchain interaction (e.g., transaction failure, token error).
    """
    def __init__(self, error_code: int, *args):
        self.error_code = error_code
        message = f"Blockchain error with code {error_code}."
        super().__init__(message, *args)

    def __str__(self):
        return f"BlockchainError: {self.message}"


class ConfigurationError(BaseError):
    """
    Raised when there is an issue with configuration loading or missing environment variables.
    """
    def __init__(self, missing_variable: str, *args):
        self.missing_variable = missing_variable
        message = f"Configuration error: Missing variable '{missing_variable}'."
        super().__init__(message, *args)

    def __str__(self):
        return f"ConfigurationError: {self.message}"


class ValidationError(BaseError):
    """
    Raised when there is a failure in validating inputs or configurations (e.g., invalid data format).
    """
    def __init__(self, field_name: str, error_details: str, *args):
        self.field_name = field_name
        self.error_details = error_details
        message = f"Validation error on '{field_name}': {error_details}"
        super().__init__(message, *args)

    def __str__(self):
        return f"ValidationError: {self.message}"
