from prompts import INTENT_CLASSIFICATION_PROMPT

class IntentClassificationAgent:
    def classify_intent(self, query: str) -> str:
        """
        Classifies the user's intent based on the query.
        """
        # In a real implementation, this would be a call to an LLM.
        # For this PoC, we'll use a simple placeholder.
        prompt = INTENT_CLASSIFICATION_PROMPT.format(query=query)
        print(f"--- Intent Classification Prompt ---\n{prompt}")

        if "plan" in query.lower():
            return "Sales, Inventory, and Procurement Recommendations"
        elif "turnover" in query.lower():
            return "Inventory Turnover and Planning Diagnostics"
        elif "stock" in query.lower():
            return "In-Stock Rate Monitoring"
        else:
            return "Unknown"
