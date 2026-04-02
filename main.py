from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import os
import uvicorn

# Optional helpers (may be created later in this branch)
try:
    from logger import setup_logging  # type: ignore
except Exception:
    setup_logging = None

try:
    from database import init_db  # type: ignore
except Exception:
    init_db = None

# Optional routers (created below)
AUTH_ROUTER = None
ARTIFACTS_ROUTER = None
TRANSCRIPTIONS_ROUTER = None
AUDIO_ROUTER = None
ANALYSIS_ROUTER = None
HERITAGE_ROUTER = None

try:
    from routes.auth_routes import router as AUTH_ROUTER  # type: ignore
except Exception:
    AUTH_ROUTER = None

try:
    from routes.artifacts_routes import router as ARTIFACTS_ROUTER  # type: ignore
except Exception:
    ARTIFACTS_ROUTER = None

try:
    from routes.transcriptions_routes import router as TRANSCRIPTIONS_ROUTER  # type: ignore
except Exception:
    TRANSCRIPTIONS_ROUTER = None

try:
    from routes.audio_routes import router as AUDIO_ROUTER  # type: ignore
except Exception:
    AUDIO_ROUTER = None

try:
    from routes.analysis_routes import router as ANALYSIS_ROUTER  # type: ignore
except Exception:
    ANALYSIS_ROUTER = None

try:
    from routes.heritage_routes import router as HERITAGE_ROUTER  # type: ignore
except Exception:
    HERITAGE_ROUTER = None

# Configure logging (fall back to basic config)
if setup_logging:
    try:
        setup_logging()
    except Exception:
        logging.basicConfig(level=logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = FastAPI(
    title=os.getenv("PROJECT_NAME", "Lens AI Platform"),
    description="Cultural Heritage Preservation Platform",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

# CORS configuration
origins_env = os.getenv("CORS_ORIGINS", "*")
if origins_env.strip() == "*":
    allow_origins = ["*"]
else:
    allow_origins = [o.strip() for o in origins_env.split(",") if o.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers if present
if AUTH_ROUTER:
    app.include_router(AUTH_ROUTER, prefix="/api/v1/auth")
if ARTIFACTS_ROUTER:
    app.include_router(ARTIFACTS_ROUTER, prefix="/api/v1/artifacts")
if TRANSCRIPTIONS_ROUTER:
    app.include_router(TRANSCRIPTIONS_ROUTER, prefix="/api/v1/transcriptions")
if AUDIO_ROUTER:
    app.include_router(AUDIO_ROUTER, prefix="/api/v1/audio")
if ANALYSIS_ROUTER:
    app.include_router(ANALYSIS_ROUTER, prefix="/api/v1/analysis")
if HERITAGE_ROUTER:
    app.include_router(HERITAGE_ROUTER, prefix="/api/v1/heritage")


@app.get("/", tags=["System"])
async def root() -> dict:
    logger.info("Root endpoint accessed")
    return {
        "platform": "Lens AI",
        "message": "Welcome to the Cultural Heritage Preservation Platform",
        "organization": "Auvra",
        "version": "1.0.0",
        "status": "operational",
    }


@app.get("/health", tags=["System"])
async def health_check() -> dict:
    return {"status": "healthy", "service": "Lens AI"}


@app.get("/api/v1/status", tags=["System"])
async def api_status() -> dict:
    return {
        "api": "operational",
        "version": "1.0.0",
        "features": [
            "artifact_management",
            "audio_transcription",
            "audio_enhancement",
            "ai_analysis",
            "heritage_preservation",
            "user_authentication",
        ],
    }


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception: %s", exc)
    if os.getenv("ENVIRONMENT", "development") == "development":
        detail = str(exc)
    else:
        detail = "An internal error occurred"
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal Server Error", "detail": detail},
    )


@app.on_event("startup")
async def startup_event() -> None:
    logger.info("Starting Lens AI application")
    if init_db:
        try:
            init_db()
            logger.info("Database initialized")
        except Exception as exc:
            logger.exception("Database initialization failed: %s", exc)


@app.on_event("shutdown")
async def shutdown_event() -> None:
    logger.info("Shutting down Lens AI application")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", 8000)),
        reload=os.getenv("ENVIRONMENT", "development") == "development",
        log_level=os.getenv("LOG_LEVEL", "info").lower(),
    )
