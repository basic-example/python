from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.orm import registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_case():
    assert User.__table__ == inspect(User).local_table
