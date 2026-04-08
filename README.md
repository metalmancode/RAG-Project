# RAG Project

A modular, stateful Artificial Intelligence chat application built with Python and LlamaIndex. This project acts as the foundational setup for an advanced Retrieval-Augmented Generation (RAG) agent. It currently demonstrates how to orchestrate a stateless Large Language Model (LLM) into an interactive, conversational chatbot with memory.

## Features

- **Interactive Chat Interface**: A command-line chat engine managed by LlamaIndex's `SimpleChatEngine`.
- **Stateful Memory**: Maintains conversational context across multiple turns.
- **Modular Architecture**: Built following Separation of Concerns to keep configurations, loaders, and core orchestration neatly divided.
- **Groq Integration**: Powered by high-speed Groq inference (currently utilizing `llama-3.3-70b-versatile`).

## Prerequisites

- **Conda**: You must have Conda (Anaconda or Miniconda) installed on your system.
- **Groq API Key**: You'll need a free API key from [Groq](https://console.groq.com/).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/metalmancode/RAG-Project.git
   cd RAG-Project
   ```

2. **Create the Conda Environment:**
   Build the environment from the provided `environment.yml` configuration.
   ```bash
   conda env create -f environment.yml
   ```

3. **Activate the Environment:**
   ```bash
   conda activate rag-project-env
   ```

## Configuration

1. In the root directory of the project, create a file named `.env`.
2. Add your Groq API key exactly as shown below:
   ```bash
   # .env
   GROQ_API_KEY="your_groq_api_key_here"
   ```
*(Note: Because of the `.gitignore` setup, your `.env` file will never be committed to Git. Never share your API keys publicly.)*

## Usage

Start the interactive chat session by executing the main entry point:

```bash
python main.py
```

*(If you experience Python path conflicts, you can use the absolute path to your active Conda environment's Python executable, e.g., `/opt/anaconda3/envs/rag-project-env/bin/python main.py`)*

Type `quit` or `exit` to end the conversation.

## Project Structure

```
├── .env                  # Private API keys and environment variables
├── .gitignore            # Files excluded from version control
├── environment.yml       # Conda dependencies and packages
├── main.py               # Main application entry point
└── src/                  # Application source code
    ├── __init__.py       # Initializes the src module
    ├── config.py         # System prompts and model parameters
    ├── engine.py         # The chat engine (orchestration layer)
    └── model_loader.py   # LLM component initialization
```
