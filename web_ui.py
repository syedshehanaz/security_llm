import streamlit as st
from agents.coordinator import run_coordinator

st.title("🔐 Cybersecurity LLM Agents Dashboard")

if st.button("Run Coordinator"):
    st.write("Running...")
    result = run_coordinator()
    st.success(result)
