# orchestrator.py

from .policy_engine import PolicyEngine
from .container_manager import ContainerManager
from .logging_config import logger

class SudoOrchestrator:
    def __init__(self, policy_engine: PolicyEngine, container_manager: ContainerManager):
        self.policy_engine = policy_engine
        self.container_manager = container_manager

    def execute_task(self, task_name: str, task_params: dict, user_token: str):
        """
        Main entry point for executing a task.
        
        1. Validates user permissions via PolicyEngine
        2. Prepares the task
        3. Executes the task within a container (via ContainerManager)
        4. Logs the result
        
        :param task_name: The name of the task to execute
        :param task_params: The parameters required for the task
        :param user_token: Token to verify user identity and permissions
        :return: Execution result or error
        """
        try:
            # Step 1: Check if the user has permission to perform the task
            if not self.policy_engine.check_permission(task_name, user_token):
                raise PermissionError(f"User does not have permission to execute task: {task_name}")
            
            # Step 2: Prepare and route the task to the container
            task = self.prepare_task(task_name, task_params)
            
            # Step 3: Execute the task inside the container
            result = self.container_manager.execute_in_container(task)
            
            # Step 4: Log the successful execution of the task
            logger.info(f"Task '{task_name}' executed successfully with result: {result}")
            
            return result

        except PermissionError as e:
            logger.error(str(e))
            return {"error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error during task execution: {str(e)}")
            return {"error": "An unexpected error occurred."}

    def prepare_task(self, task_name: str, task_params: dict):
        """
        Prepares the task, which can involve validation, parameter formatting, etc.
        
        :param task_name: The task to prepare
        :param task_params: The parameters to pass to the task
        :return: The prepared task ready for execution
        """
        # For now, let's just return the parameters as is. You could expand this logic
        # for things like data validation, transformation, etc.
        return {
            "name": task_name,
            "params": task_params
        }
