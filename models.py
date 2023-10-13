from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from database import Base

class TodoModel(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

class TagModel(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)