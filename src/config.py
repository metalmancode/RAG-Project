"""
Configuration file to manage model parameters.
"""

# --- LLM Model Configuration ---
LLM_MODEL: str = "llama-3.3-70b-versatile"
LLM_MAX_NEW_TOKENS: int = 768
LLM_TEMPERATURE: float = 0.01
LLM_TOP_P: float = 0.95
LLM_REPETITION_PENALTY: float = 1.03
# Example question, not used in the current code
# LLM_QUESTION: str = (
#     "What is the capital of France?"
# )
LLM_SYSTEM_PROMPT: str = (
    "You are a helpful chatbot. Be friendly and conversational."
)
