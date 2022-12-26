from sqlalchemy import Table, Column, Integer, String, create_engine
from sqlalchemy.orm import registry, Session
from sqlalchemy.sql.expression import text

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def to_string(query):
    return "".join(str(query).splitlines())


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)

    statement1 = session.query(User).filter(text("name like 'ab%'")).statement
    assert (
        to_string(statement1)
        == "SELECT users.id, users.name FROM users WHERE name like 'ab%'"
    )

    statement2 = (
        session.query(User).with_entities(User.id, text("name as username")).statement
    )
    assert to_string(statement2) == "SELECT users.id, name as username FROM users"
