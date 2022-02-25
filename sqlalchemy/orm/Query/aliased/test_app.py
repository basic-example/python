import logging
import re

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, aliased, registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class StreamHandler(logging.StreamHandler):
    def emit(self, record):
        if re.match("^SELECT", record.msg):
            message = "".join(str(record.msg).splitlines())
            messages.append(message)


messages = []
logging.basicConfig()
logging.getLogger("sqlalchemy").setLevel(logging.DEBUG)
logging.getLogger("sqlalchemy").addHandler(StreamHandler())


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(User(id=3, name="park"))
    session.commit()

    Query(aliased(User)).with_session(session).all()

    assert len(messages) == 1
    assert (
        "SELECT users_1.id AS users_1_id, users_1.name AS users_1_name FROM users AS users_1"
        == messages[0]
    )

    Query(aliased(User, Query(User).subquery())).with_session(session).all()

    assert len(messages) == 2
    assert (
        "SELECT anon_1.id AS anon_1_id, anon_1.name AS anon_1_name FROM (SELECT users.id AS id, users.name AS name FROM users) AS anon_1"
        == messages[1]
    )
