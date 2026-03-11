import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls.get("API_KEY_GROQ", "").strip()
            selected_groq_model = self.user_controls.get("selected_groq_model")
            
            # Use environment variable if user didn't provide key
            if not groq_api_key:
                groq_api_key = os.environ.get("GROQ_API_KEY", "").strip()
            
            # Check if we have a valid API key
            if not groq_api_key:
                st.error("⚠️ Please enter your Groq API key in the UI or set GROQ_API_KEY environment variable.")
                return None
            
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
        except Exception as e:
            st.error(f"Error initializing Groq LLM: {str(e)}")
            raise ValueError(f"Error initializing Groq LLM: {str(e)}")
        
        return llm