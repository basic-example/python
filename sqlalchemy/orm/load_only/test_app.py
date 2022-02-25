import logging
import re

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, load_only, registry, relationship, selectinload

Base = registry().generate_base()


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    path = Column(String)
    size = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", foreign_keys=[user_id], back_populates="photos")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    photos = relationship("Photo")


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
    user1 = User(id=1, name="lee", age=20)
    user2 = User(id=2, name="park", age=30)
    photo1 = Photo(id=1, user_id=1, path="aaa.jpg", size=100)
    photo2 = Photo(id=2, user_id=2, path="bbb.jpg", size=200)
    session.add(user1)
    session.add(user2)
    session.add(photo1)
    session.add(photo2)
    session.commit()
    session.query(User).options(load_only(User.name)).all()

    assert len(messages) == 1
    assert (
        messages[0]
        == "SELECT users.id AS users_id, users.name AS users_name FROM users"
    )

    session.query(User).options(
        load_only(User.id), selectinload(User.photos).load_only(Photo.path)
    ).all()

    assert len(messages) == 3
    assert messages[1] == "SELECT users.id AS users_id FROM users"
    assert re.match(
        "SELECT photos.user_id AS photos_user_id, photos.id AS photos_id, photos.path AS photos_path FROM photos WHERE photos.user_id IN",
        messages[2],
    )
