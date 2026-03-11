---
title: Agentic AI Chat Bot
emoji: 🤖
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: "1.30.0"
python_version: "3.11"
app_file: app.py
pinned: false
---
# AgenticAI ChatBot – AI News Explorer with LangGraph

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Framework-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Deployment](https://img.shields.io/badge/Deployment-HuggingFace%20Spaces-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Overview
AgenticAI ChatBot is an intelligent agentic AI application built with **LangGraph** and **LLMs** (Groq/OpenAI). It features multiple use cases including an advanced **AI News Explorer** that fetches, summarizes, and organizes AI news from around the world.

The application is deployed as an interactive web app using **Streamlit** on **Hugging Face Spaces**, providing real-time access to AI news summaries.

**🔗 Live Demo:** https://huggingface.co/spaces/mulpurisindhura942/AgenticAI_Chat_Bot

## ✨ Features
- 📰 **AI News Explorer** - Fetch and summarize AI news (Daily/Weekly/Monthly)
- 💬 **Stateful Conversations** - Maintain conversation memory across sessions
- 🛠️ **Tool-Enabled AI Agent** - Dynamically use tools to complete tasks
- 🧠 **Reasoning-Based Responses** - Advanced reasoning capabilities
- ⚡ **High-Performance Inference** - Powered by Groq & OpenAI LLMs
- 🏥 **Healthcare Chatbot** - Specialized healthcare assistance
- 🌐 **Web Search Integration** - Real-time web search with Tavily API
- 📊 **Multi-LLM Support** - Switch between Groq and OpenAI models

## 🛠️ Tech Stack
- **LLM:** Groq (whisper-large-v3-turbo) / OpenAI (gpt-4o-mini)
- **Framework:** LangGraph + LangChain
- **Programming Language:** Python 3.11
- **UI:** Streamlit
- **Deployment:** Hugging Face Spaces
- **News API:** Tavily Search API
- **Web Search:** Tavily API

## 🏗️ Architecture

```
User Input (Streamlit UI)
        ↓
LangGraph Workflow Manager
        ↓
LLM (Groq/OpenAI)
        ↓
Tool Execution & Reasoning
        ↓
Response with Memory
```

## 📁 Project Structure

```
AINEWSAgentic/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
├── .env                           # Environment variables (not in repo)
├── AINews/                        # Generated news summaries
│   ├── daily_summary.md
│   ├── weekly_summary.md
│   └── monthly_summary.md
└── src/
    └── langgraphagenticai/
        ├── main.py                # Main application logic
        ├── LLMs/
        │   ├── groqllm.py         # Groq LLM integration
        │   └── openaillm.py       # OpenAI LLM integration
        ├── nodes/
        │   ├── ai_news_node.py    # AI News fetching & summarization
        │   ├── basic_chatbot_node.py
        │   ├── chatbot_with_tool_node.py
        │   └── healthcare_node.py
        ├── graph/
        │   └── graph_builder.py   # LangGraph workflow builder
        ├── tools/
        │   └── search_tool.py     # Web search integration
        ├── ui/
        │   └── streamlitui/
        │       ├── loadui.py      # UI components
        │       └── display_result.py
        └── state/
            └── state.py           # State management
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- API Keys:
  - **Groq API Key** (free at https://console.groq.com)
  - **OpenAI API Key** (at https://platform.openai.com)
  - **Tavily API Key** (free at https://tavily.com)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Sindhura942/AgenticAI_Chat_Bot.git
cd AINEWSAgentic
```

2. **Create a virtual environment**
```bash
python -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```
GROQ_API_KEY = your_groq_api_key_here
OPENAI_API_KEY = your_openai_api_key_here
TAVILY_API_KEY = your_tavily_api_key_here
```

5. **Run the application**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 💡 Usage

### 🔑 API Keys Setup
Each user needs their **own API keys** to use the app. Get free API keys from:

- **Groq API** (Free tier available): https://console.groq.com
  - Sign up and create an API key
  - No credit card required for free tier
  
- **OpenAI API** (Paid, but affordable): https://platform.openai.com/api-keys
  - Create an account and generate API key
  - Set up billing
  
- **Tavily API** (Free tier available): https://tavily.com
  - Sign up and get your API key
  - Free tier includes search capabilities

### Using on Hugging Face Spaces
1. Visit: https://huggingface.co/spaces/mulpurisindhura942/AgenticAI_Chat_Bot
2. In the **Streamlit UI**, you'll see input fields for:
   - Select your LLM (Groq or OpenAI)
   - Enter Tavily API Key
3. Paste your own API keys in the input fields
4. The app will use YOUR keys for YOUR API calls
5. You pay for your own usage

### Using Locally
1. Create `.env` file with your keys:
```
GROQ_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```
2. Run: `streamlit run app.py`

## 📊 Features Breakdown

### AI News Explorer
- Fetches latest AI news from global sources
- Summarizes articles using LLM
- Saves summaries as markdown files
- Supports Daily, Weekly, Monthly summaries
- Organizes news by date (latest first)

### LangGraph Integration
- Stateful workflow management
- Multi-node graph architecture
- Dynamic tool integration
- Conversation memory management

### Multi-LLM Support
- **Groq**: Ultra-fast inference (recommended for speed)
- **OpenAI**: Advanced reasoning (gpt-4o-mini)

## 🔐 Security
- API keys stored in `.env` (not in repo)
- `.gitignore` protects sensitive files
- No hardcoded credentials

## 📝 Example Output

### AI News Summary
```
# Daily AI News Summary

### [2026-03-11]
- India's communications minister highlights how AI is evolving networks...
  (https://example.com/news1)

### [2026-03-10]
- New breakthrough in AI safety announced...
  (https://example.com/news2)
```

## 🌐 Deployment

### Hugging Face Spaces
The app is deployed on Hugging Face Spaces: 
**[https://huggingface.co/spaces/mulpurisindhura942/AgenticAI_Chat_Bot](https://huggingface.co/spaces/mulpurisindhura942/AgenticAI_Chat_Bot)**

To deploy your own:
1. Create a Hugging Face Space (Streamlit SDK)
2. Add your repository as a Git remote
3. Push your code
4. Add environment variables in Space settings

## 🤝 Contributing
Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📚 Learning Outcomes
- Build agentic AI systems with LangGraph
- Integrate multiple LLMs
- Create stateful conversational agents
- Deploy AI apps to production
- Work with external APIs and tools

## 🔮 Future Improvements
- [ ] Multi-agent collaboration
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Vector database for memory
- [ ] Voice input/output
- [ ] Custom knowledge base integration
- [ ] Advanced analytics dashboard

## 📄 License
MIT License - feel free to use this project for personal or commercial purposes.

## 👨‍💻 Author
**Sindhura Bhavya Mulpuri**
- GitHub: [@Sindhura942](https://github.com/Sindhura942)
- Hugging Face: [@mulpurisindhura942](https://huggingface.co/mulpurisindhura942)

## 📧 Support
For issues, questions, or suggestions, please open an issue on GitHub.

**Made with ❤️ using LangGraph, Streamlit, and AI**


