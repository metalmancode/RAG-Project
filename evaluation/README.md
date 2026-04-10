# RAG Evaluation Framework

This directory houses a purely standalone **"Test-Lab"** designed to ruthlessly evaluate your RAG application's quality using the **Ragas** metric framework. We evaluate your models quantitatively to ensure mathematical adherence rather than feeling-based chat responses.

## Core Metrics Graded
The evaluation harness generates a scorecard natively inside `evaluation_results/` that calculates:
1. **Faithfulness**: Is the LLM hallucinating? Can you trust its answers? (Determined by ensuring the generated answer is derived explicitly from the retrieved context).
2. **Answer Correctness**: Does the LLM perfectly match the factual semantics of the true answer we provided in our ground-truths?
3. **Context Precision**: How much noise is the retriever sending? High precision means the chunks sent to the LLM are dense with relevance instead of fluff.
4. **Context Recall**: Out of all the information required to perfectly answer the question, what percentage of it did the retriever successfully locate?

## How It Works

Because making evaluation calls to an external API like Groq is intensely volatile and generally breaks free-tier Rate Limits rapidly, our engine separates testing operations out cleanly:
- We initialize a **completely separate LLM and Evaluation Embedder model** (`llama-3.3-70b-versatile` and `BAAI/bge-large-en-v1.5`) via `evaluation_model_loader.py`.
- It dynamically generates its own *scratch-pad* Vector Store caching indices (`local_storage/evaluation_vector_stores`) independent of production.
- All evaluation row inquiries are systematically processed incrementally with a graceful `SLEEP_PER_EVALUATION` pause between chunks to completely bypass `langchain_core.exceptions` regarding tokens-per-minute constraints.

## Usage

You do NOT execute anything inside this directory. To run an evaluation loop, simply execute the `evaluate.py` script located at the very root of your project:

```bash
python evaluate.py
```

It will execute across your `evaluation_questions.py` suite.

## Customizing The Ground-Truths

Currently, `evaluation_questions.py` uses 6 strict questions heavily testing your ingestion of *Alice's Adventures in Wonderland*.
When you delete `alice_in_wonderland.txt` from your production `/data` folder to inject your own RAG data, you **MUST** similarly update this test harness!

1. Edit `evaluation_questions.py`
2. Formulate 5-6 hard questions explicitly pertaining to the knowledge you just added.
3. Critically, draft the exact **correct factual ground_truth** answer the system must achieve. 
4. Run `python evaluate.py`. 
5. Review your newly dynamically-generated `.csv` report in `evaluation_results/`!
