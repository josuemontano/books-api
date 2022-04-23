from typing import Any, Optional

import strawberry
from strawberry.types import Info

from ..concepts.book import Book, BookType
from .context import CustomContext
from .pagination import Connection
from .pagination.connection import build_connection


@strawberry.type
class Query:
    @strawberry.field
    def health(self) -> str:
        return "OK"

    @strawberry.field
    def books(
        self,
        info: Info[CustomContext, Any],
        first: int = 50,
        after: Optional[str] = None,
        before: Optional[str] = None,
    ) -> Connection[BookType]:
        db = info.context.db
        query = db.query(Book)
        sort_column = Book.id

        return build_connection(
            query, first, after, before, sort_column, BookType.from_db_model
        )
