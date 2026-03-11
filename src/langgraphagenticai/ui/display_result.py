import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        
        response = ""
        
        # Build message history from chat_history
        messages = []
        if "chat_history" in st.session_state:
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    messages.append(HumanMessage(content=msg["content"]))
                else:
                    messages.append(AIMessage(content=msg["content"]))
        
        # Add current user message
        messages.append(HumanMessage(content=user_message))
        
        try:
            # Stream responses from graph
            with st.spinner("Generating response..."):
                result = graph.invoke({'messages': messages})
                
                # Extract the last message from result
                if 'messages' in result:
                    messages_list = result['messages']
                    # Get the last non-human message (should be AI response)
                    for msg in reversed(messages_list):
                        if isinstance(msg, AIMessage):
                            response = msg.content
                            break
                    
                    if not response and len(messages_list) > 0:
                        response = str(messages_list[-1].content)
                    
        except Exception as e:
            print(f"Error in display_result_on_ui: {str(e)}")
            st.error(f"❌ Error streaming response: {str(e)}")
            import traceback
            st.write(f"```\n{traceback.format_exc()}\n```")
            response = f"Error: {str(e)}"
        
        return response