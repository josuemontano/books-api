from typing import Optional

import strawberry
from api.concepts.author import AuthorType as Author
from api.concepts.publisher import PublisherType as Publisher


@strawberry.type
class Book:
    id: str
    title: str
    description: Optional[str]
    isbn13: Optional[str]
    author: Author
    publisher: Publisher

    @classmethod
    def from_db_model(cls, instance):
        """Adapt this method with logic to map your orm instance to a strawberry decorated class"""
        return cls(
            id=instance.id,
            title=instance.title,
            isbn13=instance.isbn13,
            description=instance.description,
            author=instance.author,
            publisher=instance.publisher,
        )
