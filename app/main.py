from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from .database import create_db, get_session
from .models import Todo
from .schemas import TodoCreate, TodoRead
from .crud import (
    createatodo,
    getalltodos,
    getatodo,
    updateatodo,
    deleteatodo
)
from sqlmodel import Session
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    create_db()

@app.get("/todos/", response_model=List[TodoRead])
def read_todos(session: Session = Depends(get_session)):
    return getalltodos(session)

@app.get("/todo/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, session: Session = Depends(get_session)):
    todo = getatodo(session, todo_id)
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo

@app.post("/todos/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session)):
    return createatodo(todo, session)

@app.put("/todo/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoCreate, session: Session = Depends(get_session)):
    db = updateatodo(session, todo_id, todo)
    if not db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return db

@app.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    db = deleteatodo(session, todo_id)
    if not db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return
