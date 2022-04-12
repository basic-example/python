from typing import Literal, Union

import pytest
from pydantic import BaseModel, Field, ValidationError


class Bearer(BaseModel):
    auth_type: Literal["bearer"]
    token: str


class Basic(BaseModel):
    auth_type: Literal["basic"]
    username: str
    password: str


class TypedModel(BaseModel):
    credential: Union[Basic, Bearer] = Field(..., discriminator="auth_type")


class NonTypedModel(BaseModel):
    credential: Union[Basic, Bearer]


def test_case():
    TypedModel(credential={"auth_type": "bearer", "token": "abcd"})

    with pytest.raises(Exception) as exception:
        TypedModel(credential={"auth_type": "bearer"})

    assert exception.type == ValidationError
    assert "token\n  field required" in str(exception.value)
    assert "username\n  field required" not in str(exception.value)
    assert "password\n  field required" not in str(exception.value)

    with pytest.raises(Exception) as exception:
        TypedModel(credential={"auth_type": "basic"})

    assert exception.type == ValidationError
    assert "token\n  field required" not in str(exception.value)
    assert "username\n  field required" in str(exception.value)
    assert "password\n  field required" in str(exception.value)

    with pytest.raises(Exception) as exception:
        NonTypedModel(credential={"auth_type": "basic"})
    assert "token\n  field required" in str(exception.value)
    assert "username\n  field required" in str(exception.value)
    assert "password\n  field required" in str(exception.value)
