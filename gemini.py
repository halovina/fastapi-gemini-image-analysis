import google.generativeai as genai
from typing import Iterable
import os

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
}

def configure_gemini():
    genai.configure(api_key=os.getenv("APIKEY"))
    
def send_prompt_flash(fileimage, prompt: str) -> Iterable[str]:
    configure_gemini()
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash-latest",
        generation_config=generation_config,
    )
    
    chat_session = model.start_chat(
        history=[
        ]
    )
    
    response = chat_session.send_message([prompt, fileimage])
    return response