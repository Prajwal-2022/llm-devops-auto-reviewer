# 🤖 LLM DevOps Auto-Reviewer

An open-source AI-powered DevOps config file reviewer built using **LangGraph**, **Streamlit**, and **Ollama**.

## 📌 Features

- Upload or paste Terraform, YAML, or config files.
- Automatically analyze and review them using local LLMs (via Ollama).
- Provides best practices, improvement suggestions, and critiques.
- All offline — no OpenAI API needed.

## 🛠️ Stack Used

- **Streamlit** for the UI
- **LangGraph** to orchestrate reviewer, analyzer, and critic
- **Ollama** for running local LLMs like `mistral` or `llama2`
- **LangChain** Runnables to build modular LLM functions

## 🚀 How to Run Locally

1. Start your Ollama server and pull a model:

   ```bash
   ollama run mistral
