# config.py

import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists
load_dotenv()

class Config:
    """
    Centralized configuration for the environment, API endpoints, container settings, etc.
    """

    # General configurations
    APP_NAME = os.getenv("APP_NAME", "SudoAI")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
    DEBUG = os.getenv("DEBUG", "True") == "True"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # Container settings
    CONTAINER_IMAGE = os.getenv("CONTAINER_IMAGE", "sudoai/container:latest")
    CONTAINER_TIMEOUT = int(os.getenv("CONTAINER_TIMEOUT", 3600))  # in seconds

    # API settings
    API_URL = os.getenv("API_URL", "https://api.sudoai.com")
    API_KEY = os.getenv("API_KEY", "your-api-key")

    # Blockchain integration settings (if applicable)
    BLOCKCHAIN_URL = os.getenv("BLOCKCHAIN_URL", "https://blockchain.sudoai.com")
    SUDO_TOKEN = os.getenv("SUDO_TOKEN", "your-sudo-token")

    # Policy settings
    POLICY_FILE = os.getenv("POLICY_FILE", "policies.json")

    @staticmethod
    def get_env():
        """
        Returns the environment (e.g., 'development', 'production', 'testing').
        This can be used to change behavior based on the current environment.
        """
        return Config.ENVIRONMENT

    @staticmethod
    def is_production():
        """
        Returns True if the current environment is production.
        """
        return Config.ENVIRONMENT.lower() == "production"

    @staticmethod
    def is_testing():
        """
        Returns True if the current environment is testing.
        """
        return Config.ENVIRONMENT.lower() == "testing"

    @staticmethod
    def get_api_key():
        """
        Returns the API key for making requests to external services.
        """
        return Config.API_KEY

    @staticmethod
    def get_container_image():
        """
        Returns the container image to be used for running the tasks.
        """
        return Config.CONTAINER_IMAGE

    @staticmethod
    def get_container_timeout():
        """
        Returns the container timeout value (in seconds).
        """
        return Config.CONTAINER_TIMEOUT

    @staticmethod
    def get_policy_file():
        """
        Returns the path to the policy file.
        """
        return Config.POLICY_FILE
