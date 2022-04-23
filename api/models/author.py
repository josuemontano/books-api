from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import UUIDType

from ..helpers.db import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(UUIDType, primary_key=True)
    name = Column(String, nullable=False, index=True)
