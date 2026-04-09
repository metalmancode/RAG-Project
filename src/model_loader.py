import os
from dotenv import load_dotenv

from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from src.config import (
    LLM_MODEL,
    EMBEDDING_MODEL_NAME,
    EMBEDDING_CACHE_PATH,
)

# Load environment variables from the .env file
load_dotenv()


def initialise_llm() -> Groq:
    """Initialises the Groq LLM with core parameters from config."""

    api_key: str | None = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found. Make sure it's set in your .env file."
        )

    return Groq(
        api_key=api_key,
        model=LLM_MODEL,
    )

def get_embedding_model() -> HuggingFaceEmbedding:
    """
    Initialises and returns the HuggingFace embedding model.
    
    Explanation:
    An embedding model is a specialised model that converts text into a list of numbers (a vector).
    It ensures that semantically similar pieces of text have mathematically similar vectors.
    This is what allows the system to perform a "semantic search" to find relevant parts of your documents.
    """

    # Create the cache directory if it doesn't exist
    EMBEDDING_CACHE_PATH.mkdir(parents=True, exist_ok=True)

    # .as_posix() converts a file path object into a string for compatibility
    return HuggingFaceEmbedding(
        model_name=EMBEDDING_MODEL_NAME,
        cache_folder=EMBEDDING_CACHE_PATH.as_posix()
    )
