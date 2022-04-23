# Books API

Example [FastAPI](https://fastapi.tiangolo.com) app. It features:

- GraphQL API powered by [strawberry](https://strawberry.rocks)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Alembic](https://alembic.sqlalchemy.org/en/latest) migrations

## Quick start

Install Python 3.9 and [Poetry](https://python-poetry.org/docs/#installation). Then:

```bash
# Install dependencies
poetry install

# Start the server
poetry shell
uvicorn api.main:app --reload
```

Now you can make requests to the API:

```bash
curl --request POST \
  --url http://127.0.0.1:8000/graphql \
  --header 'Content-Type: application/json' \
  --data '{"query":"query { health }"}'
```
