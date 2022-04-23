from api.helpers.db import Base
from sqlalchemy import Column, String
from sqlalchemy_utils import UUIDType


class Author(Base):
    __tablename__ = "authors"

    id = Column(UUIDType, primary_key=True)
    name = Column(String, nullable=False, index=True)
