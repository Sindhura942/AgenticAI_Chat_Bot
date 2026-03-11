import os
from dotenv import load_dotenv

# Load .env from project root
load_dotenv()

from src.langgraphagenticai.main import load_langgraph_agentic_app

# Run the Streamlit app
load_langgraph_agentic_app()