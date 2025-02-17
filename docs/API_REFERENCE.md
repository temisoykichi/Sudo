# API Reference for $SUDO SDK

This document provides a detailed reference to the core classes, methods, and configuration parameters in the $SUDO SDK. Use this guide to understand the available functionality and how to integrate it into your projects.

---

## Table of Contents
1. [SudoOrchestrator](#sudoorchestrator)
2. [ContainerManager](#containermanager)
3. [BlockchainIntegration](#blockchainintegration)
4. [PolicyEngine](#policyengine)
5. [Config](#config)
6. [Errors](#errors)
7. [LoggingConfig](#loggingconfig)
8. [Utility Methods](#utility-methods)

---

## SudoOrchestrator

### Description:
The `SudoOrchestrator` class is responsible for managing AI-based workflows, determining when to invoke container-level actions, and ensuring tasks comply with security policies.

### Methods:

- **`__init__(config)`**
  - **Parameters**: `config` (Config) – Configuration object that contains necessary environment variables and settings.
  - Initializes the orchestrator with the given configuration.

- **`execute_task(task_data)`**
  - **Parameters**: `task_data` (dict) – Data describing the task to be executed (e.g., file name, action).
  - **Returns**: `task_result` (dict) – Result of the task execution, including success status and details.
  - Executes the task as described in the `task_data` dictionary, checking if it's allowed by the policy engine and managing the execution flow.

- **`verify_permissions(user_request)`**
  - **Parameters**: `user_request` (dict) – Request from the user containing details of the action they wish to perform.
  - **Returns**: `bool` – Whether the user is permitted to execute the task.
  - Verifies if the user is allowed to execute a particular task according to predefined security policies.

---

## ContainerManager

### Description:
The `ContainerManager` class manages the lifecycle of containers used to execute tasks. This includes container creation, execution, and cleanup.

### Methods:

- **`__init__(config)`**
  - **Parameters**: `config` (Config) – Configuration object containing environment and container settings.
  - Initializes the container manager with the provided configuration.

- **`create_container(task_data)`**
  - **Parameters**: `task_data` (dict) – Data that informs the container setup (e.g., required resources, actions to perform).
  - **Returns**: `container` (Container) – The created container object.
  - Creates and sets up a container for executing the task.

- **`execute_task_in_container(container, task_data)`**
  - **Parameters**: 
    - `container` (Container) – The container in which the task will be executed.
    - `task_data` (dict) – Data describing the task to execute within the container.
  - **Returns**: `task_result` (dict) – The result of the task execution inside the container.
  - Executes the specified task within the given container, including managing resource usage and access.

- **`cleanup_container(container)`**
  - **Parameters**: `container` (Container) – The container to be cleaned up.
  - Cleans up the container after the task execution is complete.

---

## BlockchainIntegration

### Description:
The `BlockchainIntegration` class provides methods for interacting with the blockchain. This may include logging task results, verifying signatures, or interacting with governance tokens.

### Methods:

- **`__init__(config)`**
  - **Parameters**: `config` (Config) – Configuration object containing blockchain settings.
  - Initializes the blockchain integration with the given configuration.

- **`log_task_execution(task_result)`**
  - **Parameters**: `task_result` (dict) – The result data from the executed task.
  - Logs the task execution result to the blockchain.

---

## PolicyEngine

### Description:
The `PolicyEngine` class enforces security policies related to which actions are allowed, denied, or logged. It interacts with the orchestrator to ensure tasks comply with predefined rules.

### Methods:

- **`__init__(config)`**
  - **Parameters**: `config` (Config) – Configuration object containing security policies and rules.
  - Initializes the policy engine with the given configuration.

- **`is_allowed(user_request)`**
  - **Parameters**: `user_request` (dict) – The request to be checked against security policies.
  - **Returns**: `bool` – Whether the request is allowed based on security policies.
  - Verifies if a user’s request is compliant with the defined security policies.

- **`log_violation(user_request)`**
  - **Parameters**: `user_request` (dict) – The request that violates security policies.
  - Logs policy violations for further review.

---

## Config

### Description:
The `Config` class manages environment variables, API settings, and configurations related to SDK operation. It centralizes configuration management for flexibility across deployments.

### Methods:

- **`__init__()`**
  - Initializes the configuration with environment variables and default settings.

- **`get(key)`**
  - **Parameters**: `key` (str) – The configuration key.
  - **Returns**: `value` (str) – The value associated with the key.
  - Retrieves the value for a specified configuration key.

- **`set(key, value)`**
  - **Parameters**: 
    - `key` (str) – The configuration key.
    - `value` (str) – The value to be set for the key.
  - Sets the value for a specified configuration key.

---

## Errors

### Description:
Custom exceptions that help standardize error handling across the SDK.

- **`PolicyViolationError`**:
  - Raised when a request violates security policies.

- **`ContainerError`**:
  - Raised when an error occurs related to container creation, execution, or cleanup.

---

## LoggingConfig

### Description:
The `LoggingConfig` class sets up structured logging for debugging and monitoring.

### Methods:

- **`__init__(log_level)`**
  - **Parameters**: `log_level` (str) – The logging level (e.g., DEBUG, INFO).
  - Initializes logging configuration with the specified log level.

- **`get_logger()`**
  - **Returns**: `logger` (Logger) – Returns a logger instance configured with the specified log level.

---

## Utility Methods

### Description:
Utility methods that provide helper functions across the SDK.

- **`validate_input(data)`**
  - **Parameters**: `data` (str) – The input data to validate.
  - **Returns**: `bool` – Whether the input data is valid.
  - Validates input data before passing it into the system.

- **`format_data(data)`**
  - **Parameters**: `data` (str) – The data to format.
  - **Returns**: `str` – The formatted data.
  - Formats data into a consistent structure for processing.

