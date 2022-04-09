import pytest
from pydantic import BaseModel, validator


class User1(BaseModel):
    name: str = None

    @validator("name")
    def validate_name(cls, value):
        raise ValueError("it is invalid")


class User2(BaseModel):
    name: str = None

    @validator("name", always=True)
    def validate_name(cls, value):
        raise ValueError("it is invalid")


def test_case():

    User1()

    with pytest.raises(Exception) as exception:
        User2()
    assert "it is invalid" in str(exception.value)
