# Contributing to $SUDO SDK

Thank you for your interest in contributing to the $SUDO SDK! We welcome contributions from the open-source community. This document outlines the guidelines and processes for contributing to this project.

---

## Table of Contents
1. [How to Contribute](#how-to-contribute)
2. [Code of Conduct](#code-of-conduct)
3. [Setting Up the Development Environment](#setting-up-the-development-environment)
4. [Coding Guidelines](#coding-guidelines)
5. [Running Tests](#running-tests)
6. [Submitting Changes](#submitting-changes)

---

## How to Contribute

We welcome contributions of all kinds, including bug fixes, feature additions, documentation improvements, and more. To contribute:

1. **Fork the repository** – Start by forking the repository to your own GitHub account.
2. **Clone your fork** – Clone the forked repository to your local machine.
3. **Create a branch** – Create a new branch for your feature or bug fix. Name the branch with a descriptive name (e.g., `feature/add-container-logging`).
4. **Make your changes** – Implement the feature or fix the bug. Follow the coding guidelines below.
5. **Commit your changes** – Commit your changes with a clear and concise commit message describing what you’ve done.
6. **Push your branch** – Push your branch to your forked repository on GitHub.
7. **Open a pull request (PR)** – Open a pull request to the main repository. Make sure to provide a detailed description of your changes in the PR.

---

## Code of Conduct

By participating in this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md). This includes treating others with respect and kindness, and fostering a positive and inclusive environment.

---

## Setting Up the Development Environment

To get started with development, you’ll need to set up your local environment.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sudo-sdk.git
   cd sudo-sdk
   ```

2. **Install dependencies**:
   For Python, make sure you have the required dependencies listed in `requirements.txt`. You can install them using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your IDE**:
   Use your preferred IDE or editor (e.g., Visual Studio Code, PyCharm) for coding. Make sure you have the Python extension installed for syntax highlighting, linting, and other features.

4. **Environment Variables**:
   If your changes require specific environment variables (e.g., API keys or configuration settings), make sure to create a `.env` file or set the variables as required.

---

## Coding Guidelines

Please follow these coding standards to maintain consistency in the project:

- **Python version**: Use Python 3.8 or higher.
- **Code style**: Follow [PEP 8](https://pep8.org/) for Python code style. If you're using an IDE, enable linting to catch style violations automatically.
- **Docstrings**: Use docstrings to document all public classes, methods, and functions. Be clear and concise in your documentation.
  - Example:
    ```python
    def my_function(param1: str) -> int:
        """
        This function does something important.

        Args:
            param1 (str): A description of the parameter.

        Returns:
            int: A description of the return value.
        """
    ```
- **Commit messages**: Write clear and concise commit messages. Use the following format:
  - **Prefix**: Use one of the following prefixes: `fix:`, `feat:`, `docs:`, `test:`.
  - **Subject**: A short description of the change.
  - **Body**: Optionally, explain the change in more detail.

  Example:
  ```bash
  feat: add support for container cleanup
  ```

---

## Running Tests

Before submitting your pull request, make sure to run tests to ensure everything works correctly.

1. **Install pytest**:
   If you haven’t already, install pytest:
   ```bash
   pip install pytest
   ```

2. **Run tests**:
   To run all tests:
   ```bash
   pytest
   ```

3. **Test coverage**:
   Ensure that your changes are covered by tests. If you are adding a new feature, write tests to verify its functionality. If you are fixing a bug, ensure there’s a test that reproduces the issue.

---

## Submitting Changes

Once you have made your changes and ensured that everything is working correctly, you can submit your pull request (PR).

1. **Ensure that your branch is up-to-date**:
   Before submitting the PR, make sure your branch is up-to-date with the latest changes in the main repository:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Open a pull request**:
   Go to the main repository and open a pull request with a clear description of what your changes do. Mention any relevant issues, if applicable.

3. **Review process**:
   After submitting your PR, it will be reviewed by the maintainers. They may request changes or improvements, and you’ll be notified if any modifications are required. Please respond to feedback promptly.

4. **Merge**:
   Once your PR is approved, it will be merged into the main branch. You will receive a notification when the merge is complete.

---

## Thank You!

We appreciate your contribution to the $SUDO SDK project! Your efforts help make this project better for everyone. If you have any questions or need help, feel free to open an issue or contact the maintainers.

