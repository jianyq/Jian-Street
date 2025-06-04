from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str

class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class QuestionnaireCreate(BaseModel):
    user_id: int
    answer: str

class Questionnaire(BaseModel):
    id: int
    user_id: int
    answer: str

    class Config:
        orm_mode = True

class ChatMessageCreate(BaseModel):
    user_id: int
    conversation_id: int
    message: str

class ChatMessage(BaseModel):
    id: int
    user_id: int
    conversation_id: int
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True
