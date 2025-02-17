# container_manager.py

import subprocess
import os
from .logging_config import logger

class ContainerManager:
    def __init__(self, container_image: str, container_network: str = 'host'):
        """
        Initializes the container manager with the desired image and network.
        
        :param container_image: The container image to use (e.g., 'python:3.9-slim')
        :param container_network: The network mode for the container (default: 'host')
        """
        self.container_image = container_image
        self.container_network = container_network
    
    def execute_in_container(self, task: dict):
        """
        Executes a task in a container.
        
        :param task: The task to execute, which includes task name and parameters
        :return: The result of the task execution
        """
        try:
            # Start the container if it's not already running (simplified version)
            container_id = self._start_container()
            
            # Execute the task inside the container
            result = self._run_task_in_container(container_id, task)
            
            # Clean up the container after execution
            self._teardown_container(container_id)
            
            return result

        except Exception as e:
            logger.error(f"Error during container execution: {str(e)}")
            return {"error": str(e)}

    def _start_container(self):
        """
        Starts a container using the configured image and network mode.
        
        :return: The container ID of the started container
        """
        try:
            # Run a container and get the container ID
            command = [
                "docker", "run", "-d", "--network", self.container_network,
                self.container_image, "sleep", "infinity"
            ]
            container_id = subprocess.check_output(command).decode('utf-8').strip()
            logger.info(f"Started container with ID: {container_id}")
            return container_id
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to start container: {str(e)}")
            raise Exception("Failed to start container")
    
    def _run_task_in_container(self, container_id: str, task: dict):
        """
        Runs the given task in the container.
        
        :param container_id: The ID of the running container
        :param task: The task to run inside the container
        :return: The result of the task execution
        """
        try:
            # Example: Run a Python script to execute the task (this could be any command)
            task_command = f'echo "{task["params"]}" > /tmp/task_output.txt'
            
            # Run the task inside the container
            command = ["docker", "exec", container_id, "bash", "-c", task_command]
            subprocess.check_output(command)
            
            # Retrieve the output from the container
            result_command = ["docker", "exec", container_id, "cat", "/tmp/task_output.txt"]
            result = subprocess.check_output(result_command).decode('utf-8').strip()
            
            logger.info(f"Task executed successfully with result: {result}")
            return result
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to run task inside container: {str(e)}")
            raise Exception("Failed to run task inside container")

    def _teardown_container(self, container_id: str):
        """
        Teardown (stop and remove) the container after execution.
        
        :param container_id: The ID of the container to remove
        """
        try:
            # Stop and remove the container
            subprocess.check_output(["docker", "rm", "-f", container_id])
            logger.info(f"Container {container_id} stopped and removed.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to teardown container {container_id}: {str(e)}")
