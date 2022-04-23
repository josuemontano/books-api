from typing import Generic, List, Optional

import strawberry
from sqlalchemy.orm import Query

from .edge import Edge
from .helpers import GenericType, decode_cursor, generate_cursor


@strawberry.type
class PageInfo:
    """Pagination context to navigate objects with cursor-based pagination

    Instead of classic offset pagination via `page` and `limit` parameters,
    here we have a cursor of the last object and we fetch items starting from that one

    Read more at:
        - https://graphql.org/learn/pagination/#pagination-and-edges
        - https://relay.dev/graphql/connections.htm
    """

    has_next_page: bool
    has_previous_page: bool
    start_cursor: Optional[str]
    end_cursor: Optional[str]


@strawberry.type
class Connection(Generic[GenericType]):
    """Represents a paginated relationship between two entities

    This pattern is used when the relationship itself has attributes.
    In a Facebook-based domain example, a friendship between two people
    would be a connection that might have a `friendshipStartTime`
    """

    total_count: int
    page_info: PageInfo
    edges: list[Edge[GenericType]]


def paginate_query(
    query: Query,
    after: Optional[str],
    before: Optional[str],
    sort_column,
):
    after = None if not after else decode_cursor(after)
    before = None if not before else decode_cursor(before)

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


def build_connection(
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
