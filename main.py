from agents.intent_classification_agent import IntentClassificationAgent
from agents.task_orchestration_agent import TaskOrchestrationAgent
from agents.data_acquisition_agent import DataAcquisitionAgent
from agents.data_analysis_agent import DataAnalysisAgent

def main():
    # User query
    query = "Generate the November sales plan for the computer Department."
    department = "computer"

    # Load SOP
    with open('sop.txt', 'r') as f:
        sop = f.read()

    # Instantiate agents
    intent_agent = IntentClassificationAgent()
    orchestration_agent = TaskOrchestrationAgent()
    acquisition_agent = DataAcquisitionAgent()
    analysis_agent = DataAnalysisAgent()

    # Step 1: Intent Classification
    intent = intent_agent.classify_intent(query)
    print(f"Intent: {intent}\n")

    # Step 2: Task Orchestration
    tasks = orchestration_agent.orchestrate_tasks(intent, sop, query)
    print(f"Tasks: {tasks}\n")

    # Step 3-5: Task Execution Loop
    observations = []
    for task in tasks:
        print(f"--- Executing Task: {task} ---")
        data = acquisition_agent.acquire_data(task, department)
        if data is not None:
            analysis_result = analysis_agent.analyze_data(task, data)
            observations.append(analysis_result)
            print(f"Analysis Result: {analysis_result}\n")
        else:
            observations.append("No data acquired for this task.")


    # Final Plan Formulation (simulated)
    print("--- Final Plan ---")
    final_plan = "Based on the analysis, the November sales plan for the computer department is as follows:\n"
    for obs in observations:
        final_plan += f"- {obs}\n"
    final_plan += "Final recommendation: Increase holiday promotion budget by 150%."
    print(final_plan)


if __name__ == "__main__":
    main()
