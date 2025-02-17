# policy_engine.py

import json
from .errors import PolicyViolationError
from .logging_config import logger

class PolicyEngine:
    def __init__(self, policy_file: str):
        """
        Initializes the PolicyEngine with a set of policies.
        
        :param policy_file: Path to the policy configuration file in JSON format
        """
        self.policies = self.load_policies(policy_file)

    def load_policies(self, policy_file: str):
        """
        Loads policies from the specified JSON file.
        
        :param policy_file: Path to the policy file (in JSON format)
        :return: A dictionary representing the loaded policies
        """
        try:
            with open(policy_file, 'r') as f:
                policies = json.load(f)
                logger.info("Policies loaded successfully.")
                return policies
        except Exception as e:
            logger.error(f"Failed to load policies from {policy_file}: {str(e)}")
            raise Exception(f"Error loading policies: {str(e)}")

    def validate_action(self, action: str, parameters: dict) -> bool:
        """
        Validates whether the specified action is allowed based on the current policies.
        
        :param action: The action that the AI is attempting to perform (e.g., "create_file")
        :param parameters: A dictionary of parameters related to the action (e.g., file path, command)
        :return: True if the action is allowed, False if blocked
        """
        try:
            # Check if the action is defined in the policies
            if action not in self.policies:
                logger.warning(f"Action '{action}' is not defined in policies.")
                return False

            action_policy = self.policies[action]

            # Check if parameters for the action are valid
            for param, value in parameters.items():
                if param in action_policy.get("restricted_parameters", []):
                    if not self.is_valid_parameter(param, value, action_policy):
                        logger.warning(f"Invalid parameter '{param}' for action '{action}'.")
                        return False

            logger.info(f"Action '{action}' is allowed.")
            return True

        except Exception as e:
            logger.error(f"Error during action validation: {str(e)}")
            raise PolicyViolationError(f"Action validation failed: {str(e)}")

    def is_valid_parameter(self, param: str, value: str, action_policy: dict) -> bool:
        """
        Validates if the provided parameter value complies with the policy rules.
        
        :param param: The parameter to validate
        :param value: The value of the parameter to validate
        :param action_policy: The policy for the action that includes restrictions
        :return: True if the parameter value is valid, False otherwise
        """
        try:
            # Implement specific rules for different types of parameters
            # For example, you could validate file paths, command types, etc.
            restricted_values = action_policy.get("restricted_values", {}).get(param, [])
            if value in restricted_values:
                logger.warning(f"Parameter value '{value}' for '{param}' is restricted.")
                return False

            return True
        except Exception as e:
            logger.error(f"Error during parameter validation for '{param}': {str(e)}")
            return False

    def block_action(self, action: str, reason: str):
        """
        Blocks the specified action and raises a PolicyViolationError.
        
        :param action: The action that is being blocked
        :param reason: The reason why the action is being blocked
        """
        logger.error(f"Action '{action}' blocked: {reason}")
        raise PolicyViolationError(f"Action '{action}' blocked: {reason}")

    def log_policy_violation(self, action: str, reason: str):
        """
        Logs a policy violation for the specified action.
        
        :param action: The action that violated the policy
        :param reason: The reason for the policy violation
        """
        logger.warning(f"Policy violation detected: Action '{action}' blocked. Reason: {reason}")

