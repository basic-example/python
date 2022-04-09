from pydantic import BaseModel, ValidationError, validator
from pydantic.fields import ModelField


class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

    @validator("password")
    def password_validator(cls, value, values, field, config):
        assert values == {"email": "info@example.com", "name": "abcd"}
        assert isinstance(field, ModelField)
        assert field.name == "password"
        assert config.orm_mode == True

        if len(value) > 7:
            return "valid password"

        raise ValueError("length is invalid")


def test_case():

    try:
        user = User(name="abcd", email="info@example.com", password="1234")
    except ValidationError as exception:
        assert "length is invalid" in str(exception)

    user = User(name="abcd", email="info@example.com", password="12345678")
    assert "valid password" == user.password
