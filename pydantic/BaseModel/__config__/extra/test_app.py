import pytest
from pydantic import BaseModel, Extra


class User(BaseModel):
    username: str
    password: str

    class Config:
        extra = Extra.forbid


def test_case():
    User(username="abcd", password="1234")

    with pytest.raises(Exception) as exception:
        User(username="abcd", password="1234", other="...")

    assert "extra fields not permitted" in str(exception.value)
