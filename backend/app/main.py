from fastapi import FastAPI

app = FastAPI(
    title="CareerAI",
    description="LLM Powered AI Career Assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CareerAI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }