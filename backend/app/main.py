from fastapi import FastAPI
from pydantic import BaseModel
from app.analyser import analyze_message
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="ScamShield API",
    description="API for detecting common scam indicators in messages",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "ScamShield API is running 🚀",
        "status": "success"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

class MessageRequest(BaseModel):
    message: str


@app.post("/analyze")
def analyze(request: MessageRequest):
    result = analyze_message(request.message)

    return result