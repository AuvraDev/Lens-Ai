from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    created_at: str

class Artifact(BaseModel):
    id: int
    user_id: int
    filename: str
    created_at: str

class Transcription(BaseModel):
    id: int
    artifact_id: int
    content: str
    created_at: str

class AudioEnhancement(BaseModel):
    id: int
    artifact_id: int
    enhanced_filename: str
    created_at: str
