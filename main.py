import json
import os
# from datetime import datetime
from logging import config
from typing import Any, Generator, List

from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi_route_logger_middleware import RouteLoggerMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal
from models import TodoModel
from schemas import TodoSchema, CreateTodoSchema

app = FastAPI()


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


with open(f"{os.path.dirname(__file__)}/logging.json", encoding="utf-8") as f:
    config.dictConfig(json.load(f))
app.add_middleware(RouteLoggerMiddleware)


@app.post("/todo", response_model=TodoSchema)
def create(todo: CreateTodoSchema, db: Session = Depends(get_db)) -> Any:
    todo_obj = jsonable_encoder(todo)
    todo_model = TodoModel(**todo_obj)
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)
    return TodoSchema.model_validate(todo_model)


@app.get("/todo", response_model=List[TodoSchema])
def read(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todo_model_list = db.query(TodoModel).offset(skip).limit(limit).all()
    todo_schema_list = [
        TodoSchema.model_validate(todo_model) for todo_model in todo_model_list
    ]
    return todo_schema_list


@app.get("/todo/{todo_id}", response_model=TodoSchema)
def read_by_id(todo_id: int, db: Session = Depends(get_db)) -> Any:
    todo_model = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo is not found")
    return TodoSchema.model_validate(todo_model)


@app.put("/todo/{todo_id}")
def update(todo_id: int, todo: CreateTodoSchema, db: Session = Depends(get_db)) -> Any:
    todo_model = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo_obj = jsonable_encoder(todo_model)
    if isinstance(todo, dict):
        update_data = todo
    else:
        update_data = todo.dict(exclude_unset=True)
    for field in todo_obj:
        if field in update_data:
            setattr(todo_model, field, update_data[field])
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)

    return Response(status_code=status.HTTP_200_OK)


@app.delete("/todo/{todo_id}")
def delete(todo_id: int, db: Session = Depends(get_db)) -> Any:
    todo = db.query(TodoModel).get(todo_id)
    db.delete(todo)
    db.commit()

    return Response(status_code=status.HTTP_200_OK)
