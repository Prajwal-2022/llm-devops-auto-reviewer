from langgraph.graph import StateGraph, END
from typing import TypedDict
from agents.analyzer_agent import analyze_code
from agents.critic_agent import critic_code
from agents.reviewer_agent import review_code

# ✅ Define schema using TypedDict
class DevOpsState(TypedDict):
    code: str
    review: str
    analysis: str
    critique: str

def build_graph():
    # ✅ Create the graph with the schema
    workflow = StateGraph(DevOpsState)

    # ✅ Add nodes
    workflow.add_node("analyze", analyze_code)
    workflow.add_node("critic", critic_code)
    workflow.add_node("reviewer", review_code)

    # ✅ Define the flow
    workflow.set_entry_point("analyze")
    workflow.add_edge("analyze", "critic")
    workflow.add_edge("critic", "reviewer")
    workflow.add_edge("reviewer", END)

    return workflow.compile()
