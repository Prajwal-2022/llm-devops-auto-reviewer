from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import Ollama
from utils.prompts import REVIEW_PROMPT

llm = Ollama(model="mistral")  # or "llama2" based on your Ollama setup

prompt = PromptTemplate(
    template=REVIEW_PROMPT,
    input_variables=["code"]
)

chain = prompt | llm | StrOutputParser()

def review_code(state):
    code = state["code"]
    response = chain.invoke({"code": code})
    return {"review": response}  # ✅ must return a dict
