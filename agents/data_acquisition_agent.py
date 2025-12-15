from prompts import DATA_ACQUISITION_PROMPT
from tools.data_tools import get_sales_data, get_inventory_data

class DataAcquisitionAgent:
    def acquire_data(self, task: str, department: str):
        """
        Acquires data based on the task description.
        """
        # In a real implementation, this would be a call to an LLM.
        # For this PoC, we'll use a simple placeholder.
        prompt = DATA_ACQUISITION_PROMPT.format(task=task)
        print(f"--- Data Acquisition Prompt ---\n{prompt}")

        if "sales" in task.lower():
            return get_sales_data(department)
        elif "inventory" in task.lower():
            return get_inventory_data(department)
        else:
            return None
