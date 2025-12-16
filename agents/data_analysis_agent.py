from prompts import DATA_ANALYSIS_PROMPT
import pandas as pd

class DataAnalysisAgent:
    def analyze_data(self, task: str, data: pd.DataFrame) -> str:
        """
        Analyzes the data and generates a report.
        """
        # In a real implementation, this would be a call to an LLM.
        # For this PoC, we'll use a simple placeholder.
        prompt = DATA_ANALYSIS_PROMPT.format(task=task)
        print(f"--- Data Analysis Prompt ---\n{prompt}")

        if "sales" in task.lower():
            # Perform a simple analysis of the sales data
            avg_sales = data['sales'].mean()
            return f"The average sales for the period were {avg_sales}."
        elif "inventory" in task.lower():
            # Perform a simple analysis of the inventory data
            avg_inventory = data['inventory_level'].mean()
            return f"The average inventory level for the period was {avg_inventory}."
        else:
            return "No analysis performed."
