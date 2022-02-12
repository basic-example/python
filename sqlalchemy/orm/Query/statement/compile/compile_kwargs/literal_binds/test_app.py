import logging
import re

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, registry

Base = registry().generate_base()
messages = []


class StreamHandler(logging.StreamHandler):
    def emit(self, record):
        if re.match("^SELECT", record.msg):
            message = "".join(str(record.msg).splitlines())
            messages.append(message)

logging.basicConfig()
logging.getLogger("sqlalchemy").setLevel(logging.DEBUG)
logging.getLogger("sqlalchemy").addHandler(StreamHandler())


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    query = Query(User)
    query = query.filter(User.name == "lee")
    statement = query.statement.compile(compile_kwargs={"literal_binds": True})
    session.execute(str(statement))
    assert len(messages) == 1
    assert (
        messages[0] == "SELECT users.id, users.name FROM users WHERE users.name = 'lee'"
    )
