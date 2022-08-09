import pytest
from pydantic import BaseModel, Extra


class User(BaseModel):
    username: str
    password: str


class UserList(BaseModel):
    __root__: list[User]

    def __iter__(self):
        return iter(self.__root__)

    def __getitem__(self, item):
        return self.__root__[item]

    def dict(self):
        return super().dict()["__root__"]


def test_case():
    user1 = User(username="abcd", password="1234")
    user2 = User(username="bcde", password="2345")
    users = UserList(__root__=[user1, user2])

    assert users.dict() == [
        {
            "username": "abcd",
            "password": "1234",
        },
        {
            "username": "bcde",
            "password": "2345",
        },
    ]
    assert users[0] == {
        "username": "abcd",
        "password": "1234",
    }
