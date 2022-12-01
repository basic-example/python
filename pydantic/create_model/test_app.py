from typing import Optional

from pydantic import create_model


def test_case():

    columns = ["users.name", "users.email"]
    UserMap = create_model(
        "UserMap",
        **{k: (Optional[str], ...) for k in columns},
    )

    assert UserMap.schema()
    assert "users.name" in UserMap.schema()["properties"].keys()
    assert "users.email" in UserMap.schema()["properties"].keys()
