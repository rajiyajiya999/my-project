import streamlit as st
import os
# Import the compiled graph execution agent from your agent/graph.py file
from agent.graph import agent 

st.set_page_config(page_title="Coder Buddy AI", layout="wide")
st.title("🤖 Coder Buddy Multi-Agent Assistant")
st.write("Type your application prompt below to see your LangGraph agents collaborate!")

# User input text field box
user_query = st.text_input(
    "What web application would you like to build?", 
    placeholder="e.g., create a simple calculator web application"
)

if st.button("Generate Code Blocks"):
    if user_query:
        with st.spinner("Agents are planning, architecting, and writing your workspace layout..."):
            try:
                # Invoke your agent graph with the prompt expected by your state variables
                result = agent.invoke({"user_prompt": user_query})
                st.success("✨ Project code generation complete!")
                st.write("Check your local 'generated_project' directory inside your repository to view the files!")
            except Exception as e:
                st.error(f"Execution warning: {e}")
    else:
        st.warning("Please input a description first.")
