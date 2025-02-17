# advanced_usage.py

from sdk.orchestrator import SudoOrchestrator
from sdk.container_manager import ContainerManager
from sdk.blockchain_integration import BlockchainIntegration
from sdk.policy_engine import PolicyEngine
from sdk.config import Config
from sdk.errors import PolicyViolationError, ContainerError

def run_advanced_workflow():
    """
    An advanced use case demonstrating a multi-step AI workflow with blockchain interaction
    and custom security policies.
    """

    # Initialize the necessary components
    config = Config()
    orchestrator = SudoOrchestrator(config)
    container_manager = ContainerManager(config)
    blockchain_integration = BlockchainIntegration(config)
    policy_engine = PolicyEngine(config)

    try:
        # Step 1: Verify user policy
        user_request = {
            "task": "create_file",
            "permissions": ["write", "execute"],
            "requested_by": "user_123"
        }

        if not policy_engine.is_allowed(user_request):
            raise PolicyViolationError("User not authorized for this task")

        print("Policy check passed")

        # Step 2: Invoke orchestrator to start a container-based task
        task_data = {"task_name": "create_file", "file_name": "example.txt", "content": "Hello World"}
        task_result = orchestrator.execute_task(task_data)

        print("Task execution result:", task_result)

        # Step 3: Handle container creation and execution
        container = container_manager.create_container(task_data)
        container_manager.execute_task_in_container(container, task_data)

        print("Task executed in container")

        # Step 4: Log transaction to blockchain (if applicable)
        blockchain_integration.log_task_execution(task_result)

        print("Blockchain logging completed")

        # Step 5: Clean up resources
        container_manager.tear_down_container(container)
        print("Container cleaned up")

    except PolicyViolationError as e:
        print(f"Policy violation: {str(e)}")
    
    except ContainerError as e:
        print(f"Container error: {str(e)}")
    
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    run_advanced_workflow()
