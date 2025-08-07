from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage
from utils.prompts import ANALYZE_PROMPT

llm = Ollama(model="mistral")

def analyze_code(state):
    code = state["code"]
    prompt = ANALYZE_PROMPT.format(code=code)
    response = llm.invoke(prompt)
    return {"analysis": response}
