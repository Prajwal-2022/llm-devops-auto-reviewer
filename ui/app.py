import streamlit as st
from langgraph.graph import StateGraph
from agents.analyzer_agent import analyze_code
from agents.critic_agent import critic_code
from agents.reviewer_agent import review_code
from graph_builder import build_graph

st.set_page_config(page_title="LLM DevOps Auto-Reviewer", layout="wide")
st.title("🤖 LLM DevOps Auto-Reviewer")
st.caption("Upload your Terraform, YAML, or config file for an AI-powered review.")

graph = build_graph()

st.markdown("#### 📂 Upload your DevOps config file")
uploaded_file = st.file_uploader(
    "Drag and drop file here",
    type=["tf", "yaml", "yml", "json"],
    help="Limit 200MB per file - TF, YAML, YML, JSON"
)

st.markdown("### 📋 Or paste your DevOps config file content below:")
text_input = st.text_area("✍️ Paste your code here (optional if file is uploaded)", height=300)

# Final input value
final_input = ""

if uploaded_file:
    final_input = uploaded_file.read().decode("utf-8")
elif text_input:
    final_input = text_input

if final_input:
    st.markdown("#### 🧾 Code to Review:")
    st.code(final_input, language="yaml")

    if st.button("🔍 Analyze"):
        with st.spinner("Analyzing with LLM agent..."):
            result = graph.invoke({"code": final_input})
            st.success("✅ Analysis Complete!")
            st.markdown("### 💡 Review Suggestions:")
            st.markdown(result["review"])
