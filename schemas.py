from typing import List
from pydantic import BaseModel, ConfigDict


class IdSchema(BaseModel):
    id:int
    model_config = ConfigDict(from_attributes=True)


class TagSchema(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)


class CreateTagSchema(BaseModel):
    name: str
    model_config = ConfigDict(from_attributes=True)


class TodoSchema(BaseModel):
    id: int
    text: str
    completed: bool
    tags: List[TagSchema] = []
    model_config = ConfigDict(from_attributes=True)


class CreateTodoSchema(BaseModel):
    text: str
    completed: bool | None = False
    model_config = ConfigDict(from_attributes=True)