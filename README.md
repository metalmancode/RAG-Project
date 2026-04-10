# Full RAG Chatbot Project

A modular, stateful Artificial Intelligence application built with Python and LlamaIndex. This project acts as the foundational setup for an advanced Retrieval-Augmented Generation (RAG) agent.

It has been upgraded to a **Full RAG System**. It processes local exterior documents into a highly searchable vector index, and smoothly retrieves and dynamically injects relevant snippets into the language model to answer complex questions based strictly on your external knowledge base! By default, the application is preloaded with data from *Alice's Adventures in Wonderland*.

## How RAG Works Here

Our system utilizes three key stages to answer a question:
1. **Indexing**: On the first run, the engine reads all documents from the `data/` folder. It splits them into digestible chunks (`CHUNK_SIZE`), logically encodes them via a mathematical embedding model (`HuggingFace sentence-transformers/all-MiniLM-L6-v2`), and structurally saves an offline cache to `local_storage/vector_store/` so you never have to re-compute them!
2. **Retrieval**: When you type a question on the terminal, the system turns your question into an embedded vector and computationally compares it to our Vector Index (Semantic Similarity Search). It aggressively grabs the `SIMILARITY_TOP_K` (most relevant) chunks.
3. **Generation**: The Llama 3 LLM magically receives both your initial question and the relevant Alice in Wonderland chunk snippets. It digests the snippets and formulates a brilliant, factually grounded final answer!

## Prerequisites

- **Conda Environment**: You must have Conda (Anaconda or Miniconda) configured.
- **Groq API Key**: You'll need an active API key from [Groq](https://console.groq.com/).

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/metalmancode/RAG-Project.git
   cd RAG-Project
   ```

2. **Setup the Conda Environment:**
   Build the environment from the provided `environment.yml`.
   ```bash
   conda env create -f environment.yml
   conda activate rag-project-env
   ```

## Configuration

1. In the root directory of the project, create a file precisely named `.env`.
2. Add your Groq API key:
   ```bash
   # .env
   GROQ_API_KEY="your_groq_api_key_here"
   ```

## Usage

Start the interactive session by executing the main entry point:

```bash
python main.py
```

*(If you experience Python path conflicts, you can use the absolute path to your Conda environment's Python executable, e.g., `/opt/anaconda3/envs/rag-project-env/bin/python main.py`)*

Type `quit` or `exit` to cleanly hang up the conversation.

## Customising The Bot Data

To add your own custom knowledge base:
1. Go into the `data/` folder, delete `alice_in_wonderland.txt`, and drop in your own texts.
2. **Crucially, delete the dynamically generated `local_storage/` folder gracefully situated in your root directory.**
3. Run `main.py`. The engine will detect that the database is missing, automatically ingest your new files, chunk them, embed them, and manufacture a brand new vector layer completely catered to you!

## Evaluating the System

This project includes a professional evaluation harness built using the Ragas framework to quantitatively measure your RAG system's **Faithfulness**, **Answer Correctness**, **Context Precision**, and **Context Recall**. 

For comprehensive documentation on running these benchmark loops, tuning the retriever hyperparameters, and measuring output without hallucination side-effects, please consult the details inside the [Evaluation Suite Documentation](evaluation/README.md).

## Project Structure

```
├── .env                  # Private API keys
├── .gitignore            # Excluded sensitive/local files
├── README.md             # Project documentation
├── environment.yml       # Conda dependencies and packages
├── evaluate.py           # Entry script to run Ragas score benchmarks
├── main.py               # Main application entry point
├── evaluation/           # Standalone Ragas test-lab framework
├── local_storage/        # Auto-generated offline database for Embeddings & Vectors!
├── data/                 # Any textual data to inject into LLMs!
└── src/                  # Application source code
    ├── config.py         # Handles systemic paths and limits uniformly
    ├── engine.py         # Advanced Memory buffering and orchestration indexing 
    └── model_loader.py   # Embedding translation and Groq injection logic
```
