from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from database import Base

class TodoModel(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
