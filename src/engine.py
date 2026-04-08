from llama_index.core.llms import ChatResponse
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.core.memory import ChatSummaryMemoryBuffer
from llama_index.llms.groq import Groq

from src.config import LLM_SYSTEM_PROMPT, CHAT_MEMORY_TOKEN_LIMIT
from src.model_loader import initialise_llm


def main_chat_loop() -> None:
    """Main chat loop for a conversational chatbot."""
    llm: Groq = initialise_llm()

    # This uses the LLM to condense old messages once the limit is reached.
    memory = ChatSummaryMemoryBuffer.from_defaults(
        chat_history=[],
        llm=llm,
        token_limit=CHAT_MEMORY_TOKEN_LIMIT
    )

    conversation: SimpleChatEngine = SimpleChatEngine.from_defaults(
        llm=llm,
        memory=memory, # This replaces the default standard buffer
        system_prompt=LLM_SYSTEM_PROMPT
    )

    conversation.chat_repl()
