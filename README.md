# Books API

This is a [FastAPI](https://fastapi.tiangolo.com) example app. It features:

- GraphQL API powered by [strawberry](https://strawberry.rocks)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Alembic](https://alembic.sqlalchemy.org/en/latest) migrations

## Quick start

Install Python 3.9 and [Poetry](https://python-poetry.org/docs/#installation). Then:

```bash
# Install dependencies
poetry install

# Spawn a shell within the virtual environment
poetry shell

# Run database migrations
alembic upgrade head

# Start the server
uvicorn api.main:app --reload
```

Now you can make requests to the API:

```bash
curl --request POST \
  --url http://127.0.0.1:8000/graphql \
  --header 'Content-Type: application/json' \
  --data '{"query":"query { health }"}'
```

## Table of Contents

- [Export the GraphQL schema](#export-the-graphql-schema)

### Export the GraphQL schema

You can export the schema of the GraphQL API. It will be described in the GraphQL schema definition language (SDL).

```bash
env $(cat .env) strawberry export-schema api.graphql:schema > schema.graphql
```
