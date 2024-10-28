import json

import jsonref
from pydantic import BaseModel


def deep_merge(dict1, dict2):
    result = dict(dict1)
    for k, v in dict2.items():
        if k in dict1 and isinstance(dict1[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(dict1[k], v)
        else:
            result[k] = v
    return result


class User(BaseModel):
    username: str
    password: str


class Book(BaseModel):
    title: str
    author: User


def test_case():
    userdict = {
        "properties": {
            "password": {"title": "Password", "type": "string"},
            "username": {"title": "Username", "type": "string"},
        },
        "required": ["username", "password"],
        "title": "User",
        "type": "object",
    }
    commondict = {
        "properties": {
            "title": {"title": "Title", "type": "string"},
        },
        "required": ["title", "author"],
        "title": "Book",
        "type": "object",
    }

    schema1 = json.loads(Book.schema_json())
    assert schema1 == deep_merge(
        commondict,
        {
            "properties": {
                "author": {"$ref": "#/definitions/User"},
            },
            "definitions": {"User": userdict},
        },
    )

    schema2 = dict(jsonref.loads(Book.schema_json()))
    del schema2["definitions"]  # unnecessary schema key
    assert schema2 == deep_merge(
        commondict,
        {
            "properties": {
                "author": userdict,
            },
        },
    )
