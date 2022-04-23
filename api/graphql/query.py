import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def health(self) -> str:
        return "OK"
