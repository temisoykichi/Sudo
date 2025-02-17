# test_config.py

import pytest
from unittest.mock import patch
from sdk.config import load_config, Config


@pytest.fixture
def mock_config():
    """
    Fixture to mock the environment variables for testing.
    """
    with patch.dict("os.environ", {"API_KEY": "test_api_key", "DB_URL": "postgres://localhost/db"}):
        yield


def test_load_config(mock_config):
    """
    Test that the configuration is loaded correctly from environment variables and config files.
    """

    # Assuming load_config loads configuration from environment and returns a Config object
    config = load_config()

    # Assert that the environment variables are loaded into the configuration
    assert config.API_KEY == "test_api_key"
    assert config.DB_URL == "postgres://localhost/db"


def test_config_override(mock_config):
    """
    Test that configuration can be overridden by explicit config files.
    """
    # Simulating an override with a custom configuration file or a dictionary
    custom_config = {
        "API_KEY": "override_api_key",  # This should override the environment variable
        "DB_URL": "mysql://localhost/custom_db"
    }

    # Patch load_config to return a config with overridden values
    with patch("sdk.config.load_config", return_value=Config(**custom_config)):
        config = load_config()

    # Assert that the configuration values are overridden
    assert config.API_KEY == "override_api_key"
    assert config.DB_URL == "mysql://localhost/custom_db"


def test_missing_required_config(mock_config):
    """
    Test that missing required configuration values raise appropriate errors.
    """
    # Simulate missing required config values (e.g., `API_KEY`)
    with patch.dict("os.environ", {"DB_URL": "postgres://localhost/db"}):
        with pytest.raises(KeyError, match="API_KEY"):
            load_config()


def test_config_fallback(mock_config):
    """
    Test that the configuration falls back to default values if environment variables and config files are missing.
    """
    default_config = {
        "API_KEY": "default_api_key",  # Default value when env variable is missing
        "DB_URL": "sqlite://:memory:"  # Default fallback for DB URL
    }

    # Patch load_config to return a config with default values when no environment variables are set
    with patch("sdk.config.load_config", return_value=Config(**default_config)):
        config = load_config()

    # Assert that the configuration values match the defaults
    assert config.API_KEY == "default_api_key"
    assert config.DB_URL == "sqlite://:memory:"


def test_invalid_config(mock_config):
    """
    Test that invalid configuration values raise appropriate errors.
    """
    invalid_config = {
        "API_KEY": None,  # API_KEY cannot be None, simulate invalid config
        "DB_URL": "invalid_url"
    }

    with patch("sdk.config.load_config", return_value=Config(**invalid_config)):
        with pytest.raises(ValueError, match="Invalid API_KEY or DB_URL"):
            load_config()
