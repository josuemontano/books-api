from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext


class CustomContext(BaseContext):
    def __init__(self, db: Session):
        self.db = db
