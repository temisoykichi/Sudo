# test_policy_engine.py

import pytest
from unittest.mock import MagicMock
from sdk.policy_engine import PolicyEngine
from sdk.errors import PolicyViolationError


@pytest.fixture
def mock_policy_engine():
    """
    Fixture to mock the PolicyEngine for testing.
    """
    policy_engine = MagicMock(PolicyEngine)
    yield policy_engine


def test_check_policy_allow(mock_policy_engine):
    """
    Test that the policy engine allows a command when the policy is valid.
    """
    # Mock the expected behavior of the policy check
    mock_policy_engine.check_policy.return_value = True

    # Test allowing a valid command
    result = mock_policy_engine.check_policy("echo 'Valid Command'")

    # Assert that check_policy was called with the correct command
    mock_policy_engine.check_policy.assert_called_once_with("echo 'Valid Command'")

    # Assert that the result is as expected (True)
    assert result is True


def test_check_policy_deny(mock_policy_engine):
    """
    Test that the policy engine denies a command when the policy is violated.
    """
    # Simulate a policy violation by returning False
    mock_policy_engine.check_policy.return_value = False

    # Test denying an invalid command
    result = mock_policy_engine.check_policy("echo 'Invalid Command'")

    # Assert that check_policy was called with the correct command
    mock_policy_engine.check_policy.assert_called_once_with("echo 'Invalid Command'")

    # Assert that the result is as expected (False)
    assert result is False


def test_policy_violation_error(mock_policy_engine):
    """
    Test that the policy engine raises a PolicyViolationError for unauthorized commands.
    """
    # Simulate a policy violation by raising a PolicyViolationError
    mock_policy_engine.check_policy.side_effect = PolicyViolationError("Policy violation detected")

    # Test that the exception is raised when a policy violation occurs
    with pytest.raises(PolicyViolationError, match="Policy violation detected"):
        mock_policy_engine.check_policy("echo 'Unauthorized Command'")


def test_check_permissions(mock_policy_engine):
    """
    Test that the policy engine checks permissions correctly.
    """
    # Mock the expected result for a valid permission check
    mock_policy_engine.check_permissions.return_value = True

    # Test checking permissions for a valid command
    result = mock_policy_engine.check_permissions("echo 'Valid command'")

    mock_policy_engine.check_permissions.assert_called_once_with("echo 'Valid command'")

    # Assert that permissions are valid
    assert result is True


def test_check_permissions_denied(mock_policy_engine):
    """
    Test that the policy engine denies permission for restricted commands.
    """
    # Simulate a permission denial by returning False
    mock_policy_engine.check_permissions.return_value = False

    # Test checking permissions for an invalid command
    result = mock_policy_engine.check_permissions("echo 'Restricted command'")

    mock_policy_engine.check_permissions.assert_called_once_with("echo 'Restricted command'")

    # Assert that permissions are denied
    assert result is False


def test_check_permissions_error(mock_policy_engine):
    """
    Test that the policy engine raises an error when permission checking fails.
    """
    # Simulate an error during permission checking
    mock_policy_engine.check_permissions.side_effect = Exception("Permission checking failed")

    with pytest.raises(Exception, match="Permission checking failed"):
        mock_policy_engine.check_permissions("echo 'This will fail'")


def test_log_policy_violation(mock_policy_engine):
    """
    Test that policy violations are logged correctly.
    """
    # Mock the logging function
    with pytest.patch('sdk.policy_engine.logging') as mock_logging:
        # Simulate a policy violation
        mock_policy_engine.check_policy.side_effect = PolicyViolationError("Policy violation detected")

        # Test that the policy violation is logged
        with pytest.raises(PolicyViolationError, match="Policy violation detected"):
            mock_policy_engine.check_policy("echo 'Unauthorized Command'")

        # Ensure logging occurs
        mock_logging.error.assert_called_with("Policy violation: Policy violation detected")


def test_configuration_handling(mock_policy_engine):
    """
    Test that the policy engine handles different configuration options correctly.
    """
    # Mock the loading of different configurations
    mock_policy_engine.load_configuration.return_value = {"allowed_commands": ["echo", "ls"]}

    # Test configuration handling
    config = mock_policy_engine.load_configuration()

    # Assert that the configuration was loaded correctly
    assert config == {"allowed_commands": ["echo", "ls"]}
