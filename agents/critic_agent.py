from langchain_community.llms import Ollama
from utils.prompts import CRITIC_PROMPT

llm = Ollama(model="mistral")

def critic_code(state):
    code = state["code"]
    prompt = CRITIC_PROMPT.format(code=code)
    response = llm.invoke(prompt)
    return {"critique": response}
