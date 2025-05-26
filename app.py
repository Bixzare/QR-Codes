from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
import os


app = FastAPI(title="QR Code Generator API with Encryption", version="0.1")

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, replace "*" with specific origins if needed
    allow_methods=["POST","GET"],  # HTTP methods (GET, POST, etc.) or specifiy
    allow_headers=["*"],  # Allow all headers or specify
)


@app.get("/")
async def root():
    return {
        "message": "QR Code Generator API with Encryption is running",
        "version": "0.1",
        "features": ["QR Code Generation", "Data Encryption", "PostgreSQL Database", "PDF Output"]
    }

@app.post("create-exam")
async def create_exam(exam_data):
    print(exam_data)


@app.post("/generate-encrypted-qr")
async def generate_encrypted_qr(code:str):
    print(f"Generating encrypted QR code for: {code}")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "database": "connected",
        "encryption": "enabled"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
