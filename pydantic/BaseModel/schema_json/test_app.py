from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class Book(BaseModel):
    title: str
    author: User


def test_case():
    assert (
        Book.schema_json()
        == '{"title": "Book", "type": "object", "properties": {"title": {"title": "Title", "type": "string"}, "author": {"$ref": "#/definitions/User"}}, "required": ["title", "author"], "definitions": {"User": {"title": "User", "type": "object", "properties": {"username": {"title": "Username", "type": "string"}, "password": {"title": "Password", "type": "string"}}, "required": ["username", "password"]}}}'
    )
