from openai import OpenAI
from google import genai
import streamlit as st



# OpenAI
def ask_openai(
        prompt,
        model = "gpt-4.1-mini",
        temperature = 0
):
    """
    Return OpenAI Chat Model
    """

    client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])
    response = client.chat.completions.create(
        model = model,
        temperature = temperature,
        messages = [
            {
                "role" : "user",
                "content" : prompt
            }
        ]
    )
    return response.choices[0].message.content

# Gemini
def ask_gemini(
        prompt,
        model = "gemini-3.5-flash",
        temperature = 0.3
):
    """
    Send prompt to Gemini.
    """
    client = genai.Client(api_key=st.secrets['GOOGLE_API_KEY'])
    response = client.models.generate_content(
        model = model,
        contents = prompt,
        config={"temperature" : temperature}
    )
    return response.text

# LLM Provider
def get_response(
        provider,
        prompt,
        temperature = 0
):
    """
    Common interface for All Models
    """

    if provider == "OpenAI":
        return ask_openai(
            prompt=prompt,
            temperature=temperature
        )
    elif provider == "Gemini":
        return ask_gemini(
            prompt=prompt,

            temperature=temperature
        )
    else:
        raise ValueError(f"Unsipported Provider : {provider}")