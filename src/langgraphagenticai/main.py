import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.LLMs.openaillm import OpenAILLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.display_result import DisplayResultStreamlit

def load_langgraph_agentic_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    """

    ##Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Initialize chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": user_message})
            
            # Display user message
            with st.chat_message("user"):
                st.write(user_message)
            
            ## Configure The LLM's
            selected_llm = user_input.get("selected_llm")
            
            if selected_llm == "Groq":
                obj_llm_config = GroqLLM(user_controls_input=user_input)
            elif selected_llm == "OpenAI":
                obj_llm_config = OpenAILLM(user_controls_input=user_input)
            else:
                st.error("Error: Invalid LLM selected.")
                return
            
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized")
                return
            
            # Initialize and set up the graph based on use case
            usecase=user_input.get("selected_usecase")

            if not usecase:
                    st.error("Error: No use case selected.")
                    return
            
            ## Graph Builder
            graph_builder=GraphBuilder(model)
            try:
                 graph=graph_builder.setup_graph(usecase)
                 
                 # Get response from graph
                 display = DisplayResultStreamlit(usecase, graph, user_message)
                 response = display.display_result_on_ui()
                 
                 if response:
                     # Add assistant response to chat history
                     st.session_state.chat_history.append({"role": "assistant", "content": response})
                     
                     # Display assistant message
                     with st.chat_message("assistant"):
                         st.write(response)
                 else:
                     st.warning("⚠️ No response received from the model")
                     
            except Exception as e:
                 st.error(f"Error: Graph set up failed- {e}")
                 return

        except Exception as e:
            st.error(f"Error: {str(e)}")
