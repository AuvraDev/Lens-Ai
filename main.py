from fastapi import FastAPI
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("Starting the FastAPI application at 2026-03-31 22:50:22 UTC")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down the FastAPI application at 2026-03-31 22:50:22 UTC")

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/health")
async def health_check():
    return {"status": "Healthy"}