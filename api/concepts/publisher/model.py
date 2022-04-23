from api.helpers.db import Base
from sqlalchemy import Column, String
from sqlalchemy_utils import UUIDType


class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(UUIDType, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
