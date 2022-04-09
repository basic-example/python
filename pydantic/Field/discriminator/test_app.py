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


class Model(BaseModel):
    credential: Union[Basic, Bearer] = Field(..., discriminator="auth_type")


def test_case():
    Model(credential={"auth_type": "bearer", "token": "abcd"})

    with pytest.raises(Exception) as exception:
        Model(credential={"auth_type": "bearer"})

    assert exception.type == ValidationError
    assert "credential -> Bearer -> token\n  field required" in str(exception.value)

    with pytest.raises(Exception) as exception:
        Model(credential={"auth_type": "basic", "bearer": "abcd"})

    assert exception.type == ValidationError
    assert "credential -> Basic -> username\n  field required" in str(exception.value)
    assert "credential -> Basic -> password\n  field required" in str(exception.value)
