import openai
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(audio_file):
    try:
        file_extension = os.path.splitext(audio_file.name)[1].lower()

        allowed_formats = [".flac", ".m4a", ".mp3", ".mp4", ".mpeg", ".mpga", ".oga", ".ogg", ".wav", ".webm"]
        if file_extension not in allowed_formats:
            return "Error: Unsupported file format"

        with tempfile.NamedTemporaryFile(delete=False, suffix=file_extension) as temp_file:
            temp_file.write(audio_file.read())
            temp_file_path = temp_file.name

        with open(temp_file_path, "rb") as file:
            transcription = openai.audio.transcriptions.create(
                model="whisper-1",
                file=file,
                response_format="text"
            )
        os.remove(temp_file_path)

        return transcription

    except Exception as e:
        return f"Error: {str(e)}"
