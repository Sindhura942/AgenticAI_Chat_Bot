# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
# Activate virtual environment
source myvenv/bin/activate

# Run the Streamlit app
streamlit run app.py
```

## Architecture

This is a LangGraph-based agentic AI chatbot with a Streamlit UI. The entrypoint is `app.py`, which calls `load_langgraph_agentic_app()` from `src/langgraphagenticai/main.py`.

**Request flow:**
1. `LoadStreamlitUI` (ui/streamlitui/loadui.py) renders sidebar controls and collects user inputs
2. `main.py` selects the LLM (Groq or OpenAI) and builds the graph for the chosen use case
3. `GraphBuilder` (graph/graph_builder.py) compiles a `StateGraph` for the selected use case
4. `DisplayResultStreamlit` invokes the compiled graph and renders the response

**Three use cases, each with a different graph topology:**
- **Basic Chatbot**: `START → chatbot → END` (single node)
- **Chatbot With Web**: `START → chatbot ↔ tools (Tavily search) → END` (conditional edges via `tools_condition`)
- **AI News**: `START → fetch_news → summarize_news → save_result → END` (sequential pipeline; saves markdown to `./AINews/{frequency}_summary.md`)

**Key modules:**
- `state/state.py` — `State(TypedDict)` with a single `messages` field using `add_messages` reducer
- `LLMs/groqllm.py`, `LLMs/openaillm.py` — thin wrappers that return `ChatGroq`/`ChatOpenAI` instances; API keys come from UI input falling back to env vars
- `tools/search_tool.py` — returns `TavilySearchResults(max_results=2)` wrapped in a `ToolNode`
- `ui/uiconfigfile.ini` — source of truth for page title, LLM options, use case names, and available models; parsed by `ui/uiconfigfile.py`
- `nodes/ai_news_node.py` — fetches up to 20 Tavily results for "Top AI technology news India and globally", summarizes with LLM, and saves markdown

## Required API Keys

Set in `.env` (already gitignored) or entered directly in the Streamlit sidebar:
- `GROQ_API_KEY` — for Groq models
- `OPENAI_API_KEY` — for OpenAI models
- Tavily API key — entered in sidebar for "Chatbot With Web" and "AI News" use cases

## Docker

```bash
docker build -t ainews-agentic .
docker run -p 8501:8501 ainews-agentic
```

The Dockerfile uses `python:3.13.5-slim`, copies `requirements.txt` and `src/`, and runs `streamlit run src/streamlit_app.py` (note: the root `app.py` is the preferred local entrypoint).

## Adding a New Use Case

1. Add the use case name to `USECASE_OPTIONS` in `ui/uiconfigfile.ini`
2. Create a node class in `nodes/`
3. Add a graph-build method in `graph/graph_builder.py`
4. Add a branch in `graph_builder.py`'s `setup_graph()` dispatcher
5. Handle the use case in `main.py`'s `load_langgraph_agentic_app()`
