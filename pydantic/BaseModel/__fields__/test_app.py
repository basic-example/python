from pydantic import BaseModel
from pydantic.fields import ModelField


class User(BaseModel):
    username: str
    password: str


def test_case():
    assert list(User.__fields__.keys()) == ["username", "password"]
    del User.__fields__["username"]
    assert User(password="1234")
