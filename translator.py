import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

LANGUAGE_MAP = {
    "Bangla": "bn",
    "Hindi": "hi",
    "Spanish": "es",
    "German": "de"
}

def translate_text(text, target_language):
    try:
        target_lang_code = LANGUAGE_MAP.get(target_language, "en")
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"Translate the following text into {target_language} ({target_lang_code})."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    
    except Exception as e:
        return f"Translation Error: {str(e)}"
