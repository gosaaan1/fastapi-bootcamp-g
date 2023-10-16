from typing import List
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean, Table
from database import Base
from sqlalchemy.orm import relationship, Mapped, mapped_column

# 双方向多対多の設定
# https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#many-to-many:~:text=True)%2C%0A)-,%E5%8F%8C%E6%96%B9%E5%90%91%E3%81%AE%E5%A4%9A%E5%AF%BE%E5%A4%9A%E3%81%AE%E8%A8%AD%E5%AE%9A,-%C2%B6

todo_and_tag = Table(
    "todo_and_tag",
    Base.metadata,
    Column("todo_id", ForeignKey("todo.id"), primary_key=True),
    Column("tag_id", ForeignKey("tag.id"), primary_key=True),
)


class TodoModel(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    completed = Column(Boolean, default=False, nullable=False)

    tags: Mapped[List['TagModel']] = relationship(secondary=todo_and_tag, back_populates="todos")


class TagModel(Base):
    __tablename__ = "tag"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    todos: Mapped[List['TodoModel']] = relationship(secondary=todo_and_tag, back_populates="tags")