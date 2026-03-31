from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS configuration
origins = ["*"]  # Adjust accordingly
app.add_middleware(CORSMiddleware,
                 allow_origins=origins,
                 allow_credentials=True,
                 allow_methods=["*"],
                 allow_headers=["*"])

# Example endpoint
@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the FastAPI application!"}

# Error handling middleware
@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f"An error occurred: {exc}")
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == '__main__':
    logger.info('Starting FastAPI application...')
    uvicorn.run(app, host="0.0.0.0", port=8000)