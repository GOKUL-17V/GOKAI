# agent_utils.py (final safe version)
import os
from dotenv import load_dotenv
from pydantic_ai.agent import Agent
from pydantic_ai.common_tools.tavily import tavily_search_tool

# Load environment variables from .env file (for local dev)
load_dotenv()

# Fetch API keys from environment or Streamlit secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Define and export the agent
agent = Agent(
    "groq:llama-3.1-8b-instant",
    tools=[tavily_search_tool(TAVILY_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results.",
)

def get_search_results(query: str) -> str:
    """Fetch search results from Tavily using the Groq LLM."""
    result = agent.run_sync(query)
    return result.output
