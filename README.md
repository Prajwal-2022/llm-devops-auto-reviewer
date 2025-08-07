# 🤖 LLM DevOps Auto-Reviewer

> An AI-powered local tool to **analyze**, **review**, and **critique** DevOps configuration files (Terraform, YAML, JSON, etc.) using LLMs like Mistral or LLaMA via **Ollama** — all on your own machine.

![LangGraph](https://img.shields.io/badge/Built%20With-LangGraph-blueviolet)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen)

---

## 🚀 Project Description

**LLM DevOps Auto-Reviewer** is a privacy-friendly, offline-first tool built using:

- 🧠 **Local LLMs** (like `mistral`, `llama2`) via [Ollama](https://ollama.com/)
- 🔁 **LangGraph** + **LangChain** for multi-agent workflow orchestration
- 📄 **Streamlit** for simple interactive UI

The tool accepts your DevOps configuration files, runs them through an **Analyzer**, **Reviewer**, and **Critic**, and shows you improvement suggestions — right from your browser.

---

## 🧱 Features

- ✅ Upload or paste Terraform / YAML / JSON code
- 🔍 Local LLM analysis — no internet or API required
- 🧠 Agent-based review: analyzer, reviewer, and critic
- 💡 Suggests improvements, optimization, and best practices
- 🛡️ Works completely offline — no data leakage

---

## 📸 UI Preview

![UI Preview](docs/screenshot.png) <!-- Replace with your actual path -->

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/llm-devops-auto-reviewer.git
cd llm-devops-auto-reviewer
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On Linux/Mac
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🔧 Local LLM Setup (Ollama)

Ensure you have [Ollama](https://ollama.com/) installed and running.

Download a model like `mistral`:

```bash
ollama pull mistral
```

You can also try:

```bash
ollama pull llama2
```

---

## 🧪 Run the App

```bash
streamlit run ui/app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📁 Folder Structure

```
llm-devops-auto-reviewer/
│
├── ui/
│   └── app.py               # Streamlit UI code
│
├── agents/
│   ├── analyzer_agent.py    # LLM Agent to analyze code
│   ├── reviewer_agent.py    # LLM Agent to review code
│   └── critic_agent.py      # LLM Agent to critique code
│
├── utils/
│   └── prompts.py           # Prompt templates
│
├── graph_builder.py         # LangGraph wiring
├── main.py                  # CLI entry point
├── requirements.txt
└── README.md
```

---

## 🧠 Technologies Used

- [LangGraph](https://docs.langchain.com/langgraph/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/)
- [Streamlit](https://streamlit.io/)
- Python 3.9+

---

## 🔒 Privacy Note

This project **does not use any cloud APIs**. Everything runs on your local machine. None of your configuration code is sent over the internet.

---

## 📌 Roadmap

- [ ] Add test cases and validation framework
- [ ] Integrate support for Dockerfiles, Helm charts
- [ ] Enable file export of suggestions
- [ ] Add support for model context protocol (MCP) architecture

---

## 🙌 Contributing

PRs and feedback are welcome! Please feel free to fork and improve the project.

---


