from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


def test_case():
    user = User(username="abcd", password="1234")

    assert {"username": "abcd", "password": "1234"} == user.dict()
