import os
import streamlit as st
from langchain_openai import ChatOpenAI


class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input

    def get_llm_model(self):
        try:
            openai_api_key = self.user_controls.get("API_KEY_OPENAI")
            selected_openai_model = self.user_controls.get("selected_openai_model")
            
            if openai_api_key == '' and os.environ.get("OPENAI_API_KEY") == '':
                st.error("⚠️ Please enter your OpenAI API key to proceed.")
            
            llm = ChatOpenAI(api_key=openai_api_key, model=selected_openai_model)
        except Exception as e:
            raise ValueError(f"Error initializing OpenAI LLM: {str(e)}")
        
        return llm