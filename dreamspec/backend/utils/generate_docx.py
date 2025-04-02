import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyAu79OHreCNdYRQAO5U7UWgyvU6ZoWbiCY"))

models = genai.list_models()
for model in models:
    print(f"{model.name} | supports: {model.supported_generation_methods}")
