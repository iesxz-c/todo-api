from sqlmodel import SQLModel
from typing import Optional

class TodoCreate(SQLModel):
    title: str
    description: Optional[str] = None

class TodoRead(SQLModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False