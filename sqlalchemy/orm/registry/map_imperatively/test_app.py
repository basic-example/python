from sqlalchemy import Column, Integer, String, Table, inspect
from sqlalchemy.orm import registry

registry = registry()

users_table = Table(
    "users",
    registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)


class User:
    pass


registry.map_imperatively(User, users_table)


def test_case():
    assert users_table == inspect(User).local_table
