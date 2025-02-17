# test_orchestrator.py

import pytest
from unittest.mock import MagicMock, patch
from sdk.orchestrator import SudoOrchestrator
from sdk.errors import PolicyViolationError


@pytest.fixture
def mock_orchestrator():
    """
    Fixture to mock the SudoOrchestrator for testing.
    """
    orchestrator = MagicMock(SudoOrchestrator)
    yield orchestrator


def test_invoke_container_action(mock_orchestrator):
    """
    Test the orchestration of invoking a container action.
    """
    # Mocking the expected results from policy engine and container manager
    mock_orchestrator.policy_engine.check_policy.return_value = True
    mock_orchestrator.container_manager.run_command_in_container.return_value = "Command executed successfully"

    # Test orchestrating a simple task
    result = mock_orchestrator.invoke_container_action("container_id_123", "echo 'Hello, World!'")

    # Assert that the orchestrator checks policy and runs the command
    mock_orchestrator.policy_engine.check_policy.assert_called_once_with("echo 'Hello, World!'")
    mock_orchestrator.container_manager.run_command_in_container.assert_called_once_with("container_id_123", "echo 'Hello, World!'")

    # Assert the result is as expected
    assert result == "Command executed successfully"


def test_policy_violation_handling(mock_orchestrator):
    """
    Test that the orchestrator correctly handles policy violations.
    """
    # Simulating a policy violation by raising PolicyViolationError
    mock_orchestrator.policy_engine.check_policy.side_effect = PolicyViolationError("Policy violation detected")

    # Test that the orchestrator raises the correct error when a policy violation occurs
    with pytest.raises(PolicyViolationError, match="Policy violation detected"):
        mock_orchestrator.invoke_container_action("container_id_123", "echo 'Unauthorized Command'")


def test_multiple_container_actions(mock_orchestrator):
    """
    Test orchestration of multiple container actions in sequence.
    """
    # Mock expected behavior
    mock_orchestrator.policy_engine.check_policy.return_value = True
    mock_orchestrator.container_manager.run_command_in_container.side_effect = [
        "First command executed",
        "Second command executed"
    ]

    # Test multiple actions
    result_1 = mock_orchestrator.invoke_container_action("container_id_123", "echo 'First Command'")
    result_2 = mock_orchestrator.invoke_container_action("container_id_123", "echo 'Second Command'")

    # Assert that the orchestrator checks policy and runs commands in sequence
    assert result_1 == "First command executed"
    assert result_2 == "Second command executed"

    mock_orchestrator.container_manager.run_command_in_container.assert_any_call("container_id_123", "echo 'First Command'")
    mock_orchestrator.container_manager.run_command_in_container.assert_any_call("container_id_123", "echo 'Second Command'")


def test_orchestrator_error_handling(mock_orchestrator):
    """
    Test that the orchestrator handles container or policy engine errors.
    """
    # Simulate an error from the container manager
    mock_orchestrator.container_manager.run_command_in_container.side_effect = Exception("Container execution failed")

    with pytest.raises(Exception, match="Container execution failed"):
        mock_orchestrator.invoke_container_action("container_id_123", "echo 'This will fail'")

    # Simulate an error from the policy engine
    mock_orchestrator.policy_engine.check_policy.side_effect = Exception("Policy engine failure")

    with pytest.raises(Exception, match="Policy engine failure"):
        mock_orchestrator.invoke_container_action("container_id_123", "echo 'Another failure'")
    

def test_check_permissions(mock_orchestrator):
    """
    Test checking permissions in the orchestrator.
    """
    # Mocking permission checking behavior
    mock_orchestrator.policy_engine.check_permissions.return_value = True

    # Test checking permissions for a valid command
    result = mock_orchestrator.check_permissions("echo 'Valid command'")

    mock_orchestrator.policy_engine.check_permissions.assert_called_once_with("echo 'Valid command'")

    # Assert that permissions are valid
    assert result is True


def test_invalid_permission_handling(mock_orchestrator):
    """
    Test handling of invalid permissions in the orchestrator.
    """
    # Simulating an invalid permission case
    mock_orchestrator.policy_engine.check_permissions.side_effect = PermissionError("Permission denied")

    # Test that the orchestrator correctly raises a permission error
    with pytest.raises(PermissionError, match="Permission denied"):
        mock_orchestrator.check_permissions("echo 'Restricted command'")


def test_orchestrator_logging(mock_orchestrator):
    """
    Test logging functionality in the orchestrator.
    """
    # Mock the logging function to capture logs
    with patch('sdk.orchestrator.logging') as mock_logging:
        mock_orchestrator.invoke_container_action("container_id_123", "echo 'Log Test'")

        # Assert that logging happened during container action invocation
        mock_logging.info.assert_called_with("Executing action on container: container_id_123 with command: echo 'Log Test'")


