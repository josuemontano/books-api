import base64
from typing import TypeVar

GenericType = TypeVar("GenericType")


def generate_cursor(identifier: str):
    encoded = f"{identifier}".encode("utf-8")
    return base64.b64encode(encoded).decode()
