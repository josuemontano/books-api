from fastapi import Depends
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter

from ..helpers.db import get_db
from .context import CustomContext
from .schema import schema


async def get_context(db: Session = Depends(get_db)):
    return CustomContext(db=db)


graphql_app = GraphQLRouter(schema, context_getter=get_context)
