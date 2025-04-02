import os
import cohere
from dotenv import load_dotenv
from utils.extract_text import extract_text_from_file

# Instead of text2emotion, we use a dummy emotion tagger (optional upgrade later)
def fake_emotion_analyzer(text):
    # Simple mock – can replace with a sentiment model later
    if "error" in text.lower():
        return {"Happy": 0, "Angry": 0.7, "Surprise": 0, "Sad": 0.3, "Fear": 0}
    elif "love" in text.lower() or "thanks" in text.lower():
        return {"Happy": 0.9, "Angry": 0, "Surprise": 0.1, "Sad": 0, "Fear": 0}
    else:
        return {"Happy": 0.5, "Angry": 0.1, "Surprise": 0.1, "Sad": 0.1, "Fear": 0.2}

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def process_file(content, filename):
    try:
        text = extract_text_from_file(content, filename)

        prompt = f"""
        You are a software requirements analyst.

        From the following input, extract:
        1. Functional Requirements
        2. Non-Functional Requirements
        3. Clarifying Questions

        Input Text:
        {text}
        """

        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )

        output = response.generations[0].text.strip()
        emotion = fake_emotion_analyzer(text)

        return {
            "requirements_output": output,
            "emotion_summary": emotion
        }

    except Exception as e:
        return {"error": str(e)}
