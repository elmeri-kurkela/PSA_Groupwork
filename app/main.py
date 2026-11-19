from sqlalchemy import text
from app.infrastructure.database.session import engine
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

@app.get("/health/db")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception:
        return {
            "status": "unhealthy",
            "database": "disconnected",
        }