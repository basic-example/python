from pydantic import BaseModel, PrivateAttr


class User(BaseModel):
    email: str
    _auth_token: str = PrivateAttr()

    def __init__(self, **data):
        super().__init__(**data)
        self._auth_token = "abcd"


def test_case():
    user = User(email="admin@example.com")

    assert user._auth_token == "abcd"
    assert "email" in user.schema()["properties"]
    assert "_auth_token" not in user.schema()["properties"]
