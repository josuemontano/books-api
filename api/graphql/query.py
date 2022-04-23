import base64
from re import L
from typing import Any, List, Optional

import strawberry
from sqlalchemy.orm import Query
from strawberry.types import Info

from ..concepts.book import Book, BookType
from .context import CustomContext
from .pagination import Connection, Edge, PageInfo
from .pagination.helpers import generate_cursor


def paginate_query(
    query: Query,
    after: Optional[str],
    before: Optional[str],
    sort_column,
):
    after = None if not after else base64.b64decode(after).decode()
    before = None if not before else base64.b64decode(before).decode()

    query = query.filter(sort_column > after) if after else query
    query = query.filter(sort_column < before) if before else query
    query = query.order_by(sort_column)
    return query


def get_page_info(has_prev_page: bool, has_next_page: bool, edges: List[Edge]):
    return PageInfo(
        has_previous_page=has_prev_page,
        has_next_page=has_next_page,
        start_cursor=edges[0].cursor if len(edges) > 0 else None,
        end_cursor=edges[-1].cursor if len(edges) > 0 else None,
    )


def connection_from_query(
    query: Query,
    limit: int,
    after: Optional[str],
    before: Optional[str],
    sort_column,
    model_to_node,
):
    paginated_query = paginate_query(query, after, before, sort_column)
    items = paginated_query.limit(limit + 1).all()

    total_count = query.count()
    has_next_page = len(items) > limit
    has_prev_page = (
        paginated_query.filter(
            sort_column < getattr(items[0], sort_column.name)
        ).count()
        > limit
    )

    edges = [
        Edge(
            node=model_to_node(item),
            cursor=generate_cursor(getattr(item, sort_column.name)),
        )
        for item in (items[:-1] if has_next_page else items)
    ]
    page_info = get_page_info(has_prev_page, has_next_page, edges)

    return Connection(total_count=total_count, page_info=page_info, edges=edges)


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

        return connection_from_query(
            query, first, after, before, sort_column, BookType.from_db_model
        )
