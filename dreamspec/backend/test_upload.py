import requests
import json

url = 'http://127.0.0.1:8000/extract/'
files = {
    'file': open('C:/Users/akash/Desktop/sample_input.txt', 'rb')  # Update path as needed
}

response = requests.post(url, files=files)
data = response.json()

if "error" in data:
    print("❌ Error:", data["error"])
else:
    print("\n📦 DreamSpec AI Output\n")

    print("📂 Functional / Non-Functional Requirements:\n")
    print(data['requirements_output'])

    print("\n❤️ Emotion Summary:")
    for emotion, score in data['emotion_summary'].items():
        percent = round(score * 100)
        print(f"- {emotion}: {percent}%")
