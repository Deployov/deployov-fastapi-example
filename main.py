from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "framework": "fastapi", "port": os.getenv("PORT", "8000")}

@app.get("/health")
def health():
    return {"status": "healthy"}
