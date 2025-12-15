from prompts import TASK_ORCHESTRATION_PROMPT

class TaskOrchestrationAgent:
    def orchestrate_tasks(self, intent: str, sop: str, query: str) -> list:
        """
        Decomposes the user's query into a series of sub-tasks based on the intent and SOP.
        """
        # In a real implementation, this would be a call to an LLM.
        # For this PoC, we'll use a simple placeholder.
        prompt = TASK_ORCHESTRATION_PROMPT.format(intent=intent, sop=sop, query=query)
        print(f"--- Task Orchestration Prompt ---\n{prompt}")

        if intent == "Sales, Inventory, and Procurement Recommendations":
            return [
                "Analyze the computer department’s historical and recent sales, traffic, and user growth, and identify the key factors influencing its performance.",
                "Analyze historical and recent sales, traffic, and user growth of the overall market and industry, and identify the key factors affecting sales.",
                "Formulate the computer department’s November sales plan and adjust it based on external information."
            ]
        elif intent == "Inventory Turnover and Planning Diagnostics":
            return [
                "Analyze historical inventory turnover rates.",
                "Detect anomalies in replenishment schedules.",
                "Provide diagnostic insights for underperforming SKUs."
            ]
        elif intent == "In-Stock Rate Monitoring":
            return [
                "Track stock levels for all products.",
                "Flag items at risk of stockouts.",
                "Alert relevant agents for replenishment."
            ]
        else:
            return []
