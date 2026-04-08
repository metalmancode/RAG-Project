from llama_index.core.llms import ChatResponse
from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.llms.groq import Groq

from src.config import LLM_SYSTEM_PROMPT
from src.model_loader import initialise_llm


def main_chat_loop() -> None:
    """Main chat loop for a conversational chatbot."""
    llm: Groq = initialise_llm()

    # Create a chat engine using the system prompt
    conversation: SimpleChatEngine = SimpleChatEngine.from_defaults(
        llm=llm,
        system_prompt=LLM_SYSTEM_PROMPT
    )

    print("--- Chat Started ---")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("--------------------")

    while True:
        user_input: str = input("\nYou: ").strip()

        if user_input.lower() in ["quit", "exit"]:
            print("\nBot: Goodbye!")
            break

        if not user_input:
            continue

        response: ChatResponse = conversation.chat(user_input)
        print(f"\nBot: {response}")
