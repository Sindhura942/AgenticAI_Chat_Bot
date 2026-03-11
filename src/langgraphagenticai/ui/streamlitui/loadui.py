import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state["timeframe"] = ''
        st.session_state["IsFetchButtonClicked"] = False

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            # ---------- GROQ ----------
            st.subheader("Groq Settings")

            groq_models = self.config.get_groq_model_options()
            self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model", groq_models)

            # Load API key from .env, but allow user to enter their own
            self.user_controls["API_KEY_GROQ"] = os.environ.get("GROQ_API_KEY", "")
            
            # Let user enter their Groq API key in the UI
            groq_api_input = st.text_input(
                "🔑 Groq API Key",
                value=self.user_controls["API_KEY_GROQ"],
                type="password",
                help="Get your free API key from https://console.groq.com"
            )
            if groq_api_input:
                self.user_controls["API_KEY_GROQ"] = groq_api_input
            
            if not self.user_controls["API_KEY_GROQ"]:
                st.info("ℹ️ Please enter your Groq API key (free at https://console.groq.com)")

            # ---------- OPENAI ----------
            st.subheader("OpenAI Settings")

            openai_models = self.config.get_openai_model_options()
            self.user_controls["selected_openai_model"] = st.selectbox("Select OpenAI Model", openai_models)

            # Load API key from .env, but allow user to enter their own
            self.user_controls["API_KEY_OPENAI"] = os.environ.get("OPENAI_API_KEY", "")
            
            # Let user enter their OpenAI API key in the UI
            openai_api_input = st.text_input(
                "🔑 OpenAI API Key",
                value=self.user_controls["API_KEY_OPENAI"],
                type="password",
                help="Get your API key from https://platform.openai.com/api-keys"
            )
            if openai_api_input:
                self.user_controls["API_KEY_OPENAI"] = openai_api_input
            
            if not self.user_controls["API_KEY_OPENAI"]:
                st.info("ℹ️ Please enter your OpenAI API key (get it from https://platform.openai.com/api-keys)")

            # Usecase selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] =="Chatbot With Web" or self.user_controls["selected_usecase"] =="AI News" :
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("TAVILY API KEY",type="password")

            # ---------- TAVILY ----------
            ## st.subheader("Tavily Settings")

            # Only check if selected usecase needs it
            #if self.user_controls["selected_usecase"] in ["Chatbot With Web", "AI News"]:
                #self.user_controls["TAVILY_API_KEY"] = os.environ.get("TAVILY_API_KEY", "")
                #if not self.user_controls["TAVILY_API_KEY"]:
                    #st.error("⚠️ TAVILY_API_KEY not found in .env file")
                 # Validate API key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")

            if self.user_controls['selected_usecase'] == "AI News":
                st.subheader("📰 AI News Explorer")
                
                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state["IsFetchButtonClicked"] = True
                    st.session_state["timeframe"] = time_frame

        return self.user_controls