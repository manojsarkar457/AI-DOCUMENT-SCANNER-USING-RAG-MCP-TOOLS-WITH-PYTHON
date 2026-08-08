from utils.prompts import RAG_PROMPT
from utils.llm_provider import get_response
from mcp_tools.rag_tool import (build_vector_database, get_context, get_sources)

def process_pdf(file_paths, provider="OpenAI"):
    total_chunks = build_vector_database(
        file_paths=file_paths,
        provider=provider
    )
    return f"PDFs Processed successfully."

def ask_pdf(question, provider="OpenAI"):
    context = get_context(question, provider)
    if context == "":
        return(
            "I couldn't find that information "
            "in the uploaded documents."
        )
    prompt = RAG_PROMPT.format(
        context=context,
        question=question
        )

    answer = get_response(
        provider=provider,
        prompt=prompt
    )

    sources = get_sources(question, provider)

    if sources:
        answer += "\n\n**Sources:**"
        for source in sources:
            answer += f"- {source}\n"
    return answer