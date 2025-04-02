from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from requirement_engine import process_file
from dotenv import load_dotenv

# Load .env variables (like COHERE_API_KEY)
load_dotenv()

app = FastAPI()

# Enable CORS (for future frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract/")
async def extract(file: UploadFile = File(...)):
    content = await file.read()
    filename = file.filename
    result = process_file(content, filename)
    return result
