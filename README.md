# Books API

Example [FastAPI](https://fastapi.tiangolo.com) app. It features:

- GraphQL API powered by [strawberry](https://strawberry.rocks)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Alembic](https://alembic.sqlalchemy.org/en/latest) migrations

## Quick start

```bash
poetry install
uvicorn api.main:app --reload
```

Then make a request to the API:

```bash
curl --request POST \
  --url http://127.0.0.1:8000/graphql \
  --header 'Content-Type: application/json' \
  --data '{"query":"query { health }"}'
```
