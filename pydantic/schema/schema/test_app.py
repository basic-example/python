from pydantic import BaseModel
from pydantic.schema import schema


class User(BaseModel):
    username: str
    password: str


def test_case():
    user = User(username="abcd", password="1234")

    assert user.schema() == {
        "title": "User",
        "type": "object",
        "properties": {
            "username": {"title": "Username", "type": "string"},
            "password": {"title": "Password", "type": "string"},
        },
        "required": ["username", "password"],
    }
    assert schema([User]) == {
        "definitions": {
            "User": {
                "title": "User",
                "type": "object",
                "properties": {
                    "username": {"title": "Username", "type": "string"},
                    "password": {"title": "Password", "type": "string"},
                },
                "required": ["username", "password"],
            }
        }
    }
