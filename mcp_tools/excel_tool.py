from utils.prompts import RAG_PROMPT
from utils.llm_provider import get_response

from mcp_tools.rag_tool import (build_vector_database, get_context, get_sources)

def process_excel(file_paths, provider="OpenAI"):
    total_chunks = build_vector_database(file_paths=file_paths, provider=provider)
    return f"Excel Processed successfully."

def ask_excel(question, provider="OpenAI"):
    context = get_context(question=question, provider=provider)

    if not context:
        return (
            "I couldn't find that information "
            "in the uploaded Excel documents."
        )
    prompt = RAG_PROMPT.format(
        context = context,
        question = question
    )

    answer = get_response(
        provider=provider,
        prompt=prompt
    )

    sources = get_sources(
        question = question,
        provider = provider
    )

    if sources:
        answer += "\n\n**Sources:**"
        for source in sources:
            answer += f"- {source}\n"
    return answer