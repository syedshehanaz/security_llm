import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent

from tools.pdf_summary import pdf_summary_tool
from tools.log_analyzer import log_analyzer_tool
from tools.threat_search import threat_search_tool

llm = ChatOpenAI(
    temperature=0,
    model="gpt-4",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

tools = [pdf_summary_tool, log_analyzer_tool, threat_search_tool]

coordinator = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

def run_coordinator():
    query = "Analyze the PDF report and check logs for anomalies"
    response = coordinator.run(query)
    return f"[Coordinator]: {response}"
