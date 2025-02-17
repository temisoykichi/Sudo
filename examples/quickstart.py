# Import necessary components from the SDK
from sdk.orchestrator import SudoOrchestrator
from sdk.container_manager import ContainerManager
from sdk.config import Config
from sdk.errors import PolicyViolationError

# Create an instance of the configuration
config = Config()

# Initialize the orchestrator and container manager with the configuration
orchestrator = SudoOrchestrator(config)
container_manager = ContainerManager(config)

# Define a simple task (for example, create a text file in the container)
task_data = {
    "action": "create_file",
    "file_name": "hello.txt",
    "content": "Hello, world!",
}

# Run the task using the orchestrator (AI performs the task in a container)
try:
    # Ensure the task is allowed by the policy engine (automatically handled by the orchestrator)
    task_result = orchestrator.execute_task(task_data)
    
    # The task should now be executed within the container
    print(f"Task successfully executed: {task_result}")
    
    # Optionally, log this task to the blockchain (if blockchain integration is enabled)
    # from sdk.blockchain_integration import BlockchainIntegration
    # blockchain_integration = BlockchainIntegration(config)
    # blockchain_integration.log_task_execution(task_result)
    
except PolicyViolationError as e:
    print(f"Policy violation error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
