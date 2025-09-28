from pydantic import BaseModel, Field
from datetime import datetime


class TaskCreate(BaseModel):
    name: str 
    command: str 

class TaskResponse(BaseModel):
    id: int
    name: str
    command: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
    