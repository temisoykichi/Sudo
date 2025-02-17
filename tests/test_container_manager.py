# test_container_manager.py

import pytest
from unittest.mock import patch, MagicMock
from sdk.container_manager import ContainerManager, ContainerError


@pytest.fixture
def mock_container_manager():
    """
    Fixture to mock the ContainerManager for testing.
    """
    container_manager = MagicMock(ContainerManager)
    yield container_manager


def test_create_container(mock_container_manager):
    """
    Test the creation of a container.
    """
    mock_container_manager.create_container.return_value = "container_id_123"

    container_id = mock_container_manager.create_container("python:3.8-slim")

    # Assert that the create_container method was called with the expected argument
    mock_container_manager.create_container.assert_called_once_with("python:3.8-slim")
    
    # Assert that the returned container ID matches the expected mock value
    assert container_id == "container_id_123"


def test_run_command_in_container(mock_container_manager):
    """
    Test running a command inside a container.
    """
    mock_container_manager.run_command_in_container.return_value = "Command executed successfully"

    result = mock_container_manager.run_command_in_container("container_id_123", "echo 'Hello, World!'")

    # Assert that the run_command_in_container method was called with the correct arguments
    mock_container_manager.run_command_in_container.assert_called_once_with("container_id_123", "echo 'Hello, World!'")
    
    # Assert that the command result is as expected
    assert result == "Command executed successfully"


def test_save_files_to_container(mock_container_manager):
    """
    Test saving files to a container.
    """
    mock_container_manager.save_files_to_container.return_value = True

    result = mock_container_manager.save_files_to_container("container_id_123", "/path/to/file.txt")

    # Assert that save_files_to_container was called with the correct arguments
    mock_container_manager.save_files_to_container.assert_called_once_with("container_id_123", "/path/to/file.txt")
    
    # Assert the method returns True indicating success
    assert result is True


def test_tear_down_container(mock_container_manager):
    """
    Test tearing down a container.
    """
    mock_container_manager.tear_down_container.return_value = "container_id_123 destroyed"

    result = mock_container_manager.tear_down_container("container_id_123")

    # Assert that tear_down_container was called with the correct container ID
    mock_container_manager.tear_down_container.assert_called_once_with("container_id_123")
    
    # Assert the result indicates the container was destroyed
    assert result == "container_id_123 destroyed"


def test_container_error_handling(mock_container_manager):
    """
    Test error handling in container management.
    """
    # Simulate a container error when running a command
    mock_container_manager.run_command_in_container.side_effect = ContainerError("Container failure")

    # Assert that the error is properly raised when running a command in a container
    with pytest.raises(ContainerError, match="Container failure"):
        mock_container_manager.run_command_in_container("container_id_123", "echo 'This will fail'")


def test_container_cleanup_after_error(mock_container_manager):
    """
    Test that containers are cleaned up after encountering an error.
    """
    mock_container_manager.create_container.return_value = "container_id_123"
    mock_container_manager.tear_down_container.return_value = "container_id_123 destroyed"

    # Simulate an error during container usage
    mock_container_manager.run_command_in_container.side_effect = ContainerError("Container failure")

    try:
        # Create container and run a command (which will fail)
        container_id = mock_container_manager.create_container("python:3.8-slim")
        mock_container_manager.run_command_in_container(container_id, "echo 'This will fail'")
    except ContainerError:
        # Assert that the container is torn down after the error
        mock_container_manager.tear_down_container.assert_called_once_with("container_id_123")
