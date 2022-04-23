from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from ..helpers.db import Base
from .author import Author


class Book(Base):
    __tablename__ = "books"

    id = Column(UUIDType, primary_key=True)
    title = Column(String(100), nullable=False, index=True)
    description = Column(String(255))
    isbn13 = Column(String(13))
    author_id = Column(UUIDType, ForeignKey("authors.id"), nullable=False)

    author = relationship(Author)
