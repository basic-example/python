import logging
import re

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import (Session, contains_eager, defer, registry,
                            relationship, selectinload)

Base = registry().generate_base()


class UserInfo(Base):
    __tablename__ = "user_infos"
    id = Column(Integer, primary_key=True)
    type = Column(String)
    value = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", foreign_keys=[user_id], back_populates="infos")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    infos = relationship("UserInfo")


class StreamHandler(logging.StreamHandler):
    def emit(self, record):
        if re.match("^SELECT", record.msg):
            message = "".join(str(record.msg).splitlines())
            print(message)
            messages.append(message)


messages = []
logging.basicConfig()
logging.getLogger("sqlalchemy").setLevel(logging.DEBUG)
logging.getLogger("sqlalchemy").addHandler(StreamHandler())


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    user1 = User(id=1, name="lee")
    user_info1 = UserInfo(id=1, user_id=1, type="a", value="aaa")
    user_info2 = UserInfo(id=2, user_id=1, type="b", value="bbb")
    session.add(user1)
    session.add(user_info1)
    session.add(user_info2)
    session.commit()
    query = session.query(User).join(User.infos).filter(UserInfo.value=="aaa")

    user1 = query.options(selectinload(User.infos)).first()
    assert len(user1.infos) == 2

    user1 = query.options(contains_eager(User.infos)).first()
    assert len(user1.infos) == 2 # invalid result
    session.expunge_all() # or session.expunge(user1)
    user1 = query.options(contains_eager(User.infos)).first()
    assert len(user1.infos) == 1 # vaild result
