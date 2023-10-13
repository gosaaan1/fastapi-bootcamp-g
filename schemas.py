from typing import Union
from pydantic import BaseModel, ConfigDict

class TodoSchema(BaseModel):
    id: int
    text: str
    completed: bool
    model_config = ConfigDict(from_attributes=True)


class CreateTodoSchema(BaseModel):
    text: str
    completed: Union[bool, None] = False
    model_config = ConfigDict(from_attributes=True)