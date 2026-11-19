
from fastapi import FastAPI

app = FastAPI(
    title="ComicBookstore API",
    description="Backend API for the second-hand comic bookstore management system.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ComicBookstore API",
        "status": "running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
