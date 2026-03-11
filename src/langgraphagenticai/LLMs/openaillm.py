import os
import streamlit as st
from langchain_openai import ChatOpenAI


class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls.get("API_KEY_OPENAI", "").strip()
            selected_openai_model = self.user_controls.get("selected_openai_model")
            
            # Use environment variable if user didn't provide key
            if not openai_api_key:
                openai_api_key = os.environ.get("OPENAI_API_KEY", "").strip()
            
            # Check if we have a valid API key
            if not openai_api_key:
                st.error("⚠️ Please enter your OpenAI API key in the UI or set OPENAI_API_KEY environment variable.")
                return None
            
            llm = ChatOpenAI(api_key=openai_api_key, model=selected_openai_model)
        except Exception as e:
            st.error(f"Error initializing OpenAI LLM: {str(e)}")
            raise ValueError(f"Error initializing OpenAI LLM: {str(e)}")
        
        return llm