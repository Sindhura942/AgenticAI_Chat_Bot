import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls.get("API_KEY_GROQ")
            selected_groq_model = self.user_controls.get("selected_groq_model")
            
            # Debug: Print to verify values
            print(f"API Key type: {type(groq_api_key)}, value: {groq_api_key}")
            print(f"Model type: {type(selected_groq_model)}, value: {selected_groq_model}")
            
            if not groq_api_key:
                raise ValueError("Groq API key is empty or missing")
            
            llm = ChatGroq(api_key=groq_api_key, model=selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error initializing Groq LLM: {str(e)}")
        
        return llm