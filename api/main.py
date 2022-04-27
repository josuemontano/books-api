from dotenv import load_dotenv
from fastapi import FastAPI

# Add code that uses environment variables AFTER THE NEXT LINE
load_dotenv()

from .graphql import graphql_app

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
app.add_websocket_route("/graphql", graphql_app)
