from typing import Generic

import strawberry

from .helpers import GenericType


@strawberry.type
class Edge(Generic[GenericType]):
    """An edge may contain additional information of the relationship. This is the trivial case"""

    node: GenericType
    cursor: str

    def __init__(self, node: GenericType, cursor: str):
        self.node = node
        self.cursor = cursor
