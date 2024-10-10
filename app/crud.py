#get todo
#get todos
#create todo
#update todo
#delete todo

from typing import List,Optional
from sqlmodel import Session,select
from .models import Todo
from .schemas import TodoCreate,TodoRead

def createatodo(todo: TodoCreate ,session : Session):
    db=Todo.from_orm(todo)
    session.add(db)
    session.commit()
    session.refresh(db)
    return db

def getalltodos(session:Session) -> List[Todo]:
    p=select(Todo)
    results = session.exec(p)
    return results.all()

def getatodo(session:Session,todo_id:int) -> Optional[Todo]:
    return session.get(Todo,todo_id)

def updateatodo (session:Session,todo_id:int, todo:TodoCreate) -> Optional[Todo]:
    existing = session.get(Todo,todo_id)
    if existing :
        existing.title = todo.title
        existing.description = todo.description
        session.add(existing)
        session.commit()
        session.refresh(existing)
    return existing

def deleteatodo (session:Session,todo_id:int) -> bool:
    todo = session.get(Todo, todo_id)
    if todo:
        session.delete(todo)
        session.commit()
        return True
    else:
        return False