from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine,
                        select)
from sqlalchemy.orm import registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    path = Column(String)


def to_string(query):
    return "".join(str(query).splitlines())


def test_case():
    query = select(User).join_from(User, Photo)

    assert (
        "SELECT users.id, users.name FROM users JOIN photos ON users.id = photos.user_id"
        == to_string(query)
    )
