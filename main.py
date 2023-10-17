import json
import os
from logging import config
from typing import Any, Generator, List

from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi_route_logger_middleware import RouteLoggerMiddleware
from sqlalchemy.orm import Session, joinedload

from database import SessionLocal
from models import TodoModel, TagModel, todo_and_tag
from schemas import IdSchema
from schemas import CreateTagSchema, TagSchema, TagWithTodoSchema
from schemas import CreateTodoSchema, TodoSchema, TodoWithTagSchema

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


@app.post("/todo", response_model=IdSchema)
def create_todo(todo: CreateTodoSchema, db: Session = Depends(get_db)) -> Any:
    todo_obj = jsonable_encoder(todo)
    todo_model = TodoModel(**todo_obj)
    db.add(todo_model)
    db.commit()
    db.refresh(todo_model)

    return TodoSchema.model_validate(todo_model)


@app.get("/todo", response_model=List[TodoSchema])
def read_todo(skip: int = 0, limit: int = 100, completed: bool = True, db: Session = Depends(get_db)) -> Any:
    todo_model_list = db.query(TodoModel) \
        .filter(TodoModel.completed == completed) \
        .offset(skip).limit(limit).all()

    todo_schema_list = [
        TodoSchema.model_validate(todo_model) for todo_model in todo_model_list
    ]
    return todo_schema_list


@app.get("/todo/{todo_id}", response_model=TodoWithTagSchema)
def read_todo_by_id(todo_id: int, db: Session = Depends(get_db)) -> Any:
    todo_model = db.query(TodoModel) \
        .outerjoin(todo_and_tag) \
        .outerjoin(TagModel) \
        .options(joinedload(TodoModel.tags)) \
        .filter(TodoModel.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail="Todo is not found")
    return TodoWithTagSchema.model_validate(todo_model)


@app.put("/todo/{todo_id}")
def update_todo(todo_id: int, todo: CreateTodoSchema, db: Session = Depends(get_db)) -> Any:
    todo_model = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if not todo_model:
        raise HTTPException(status_code=404, detail="Todo not found")

    # TODO リファクタリングできそう...
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

    return TodoSchema.model_validate(todo_model)


@app.delete("/todo/{todo_id}", response_model=IdSchema)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> Any:
    todo = db.query(TodoModel).get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()

    return TodoSchema.model_validate(todo)


@app.post("/tag", response_model=IdSchema)
def create_tag(tag: CreateTagSchema, db: Session = Depends(get_db)) -> Any:
    tag_obj = jsonable_encoder(tag)
    tag_model = TagModel(**tag_obj)
    db.add(tag_model)
    db.commit()
    db.refresh(tag_model)

    return TagSchema.model_validate(tag_model)


@app.get("/tag", response_model=List[TagSchema])
def read_tag(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Any:
    tag_model_list = db.query(TagModel).offset(skip).limit(limit).all()
    tag_schema_list = [
        TagSchema.model_validate(tag_model) for tag_model in tag_model_list
    ]
    return tag_schema_list

@app.get("/tag/{tag_id}", response_model=TagWithTodoSchema)
def read_tag_by_id(tag_id: int, db: Session = Depends(get_db)) -> Any:
    tag_model = db.query(TagModel).filter(TagModel.id == tag_id) \
        .outerjoin(todo_and_tag) \
        .outerjoin(TodoModel) \
        .options(joinedload(TagModel.todos)).first()
    if not tag_model:
        raise HTTPException(status_code=404, detail="Tag not found")

    return TagWithTodoSchema.model_validate(tag_model)


@app.put("/tag/{tag_id}")
def update_tag(tag_id: int, tag: CreateTagSchema, db: Session = Depends(get_db)) -> Any:
    tag_model = db.query(TagModel).filter(TagModel.id == tag_id).first()
    if not tag_model:
        raise HTTPException(status_code=404, detail="Tag not found")
    for f, v in tag.model_dump(exclude_unset=True).items():
        setattr(tag_model, f, v)
    db.add(tag_model)
    db.commit()
    db.refresh(tag_model)

    return TagSchema.model_validate(tag_model)

@app.delete("/tag/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)) -> Any:
    tag = db.query(TagModel).get(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    db.delete(tag)
    db.commit() 

    return Response(status_code=status.HTTP_200_OK)
