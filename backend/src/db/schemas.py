from pydantic import BaseModel, Field, HttpUrl
from typing import List, Optional, Dict, Any
from datetime import datetime

class AIProviderCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    api_url: HttpUrl
    module_path: str = Field(..., min_length=1)
    class_name: str = Field(..., min_length=1)
    api_key: str = Field(..., min_length=1)
    config: Dict[str, Any] = {}
    is_active: bool = True

class AIProvider(BaseModel):
    id: int
    name: str
    description: Optional[str]
    api_url: HttpUrl
    module_path: str
    class_name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    content: str = Field(..., min_length=1)
    category: Optional[str] = Field(None, max_length=50)
    tags: Optional[List[str]] = []

class Question(BaseModel):
    id: int
    content: str
    category: Optional[str]
    tags: Optional[List[str]]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class CampaignCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    status: str = Field(..., regex=r'^(pending|running|completed|failed)$')
    config: Dict[str, Any] = {}

class Campaign(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str
    config: Dict[str, Any]
    created_at: datetime
    started_at: Optional[datetime]
    completed_at: Optional[datetime]

    class Config:
        orm_mode = True

class CampaignResultCreate(BaseModel):
    campaign_id: int
    question_id: int
    ai_provider_id: int
    response: str
    tokens_count: int
    response_time: float
    error: Optional[str]

class CampaignResult(BaseModel):
    id: int
    campaign_id: int
    question_id: int
    ai_provider_id: int
    response: str
    tokens_count: int
    response_time: float
    error: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True