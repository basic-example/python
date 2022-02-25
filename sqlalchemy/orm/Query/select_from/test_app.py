import logging
import re

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, defer, registry, relationship

Base = registry().generate_base()


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    path = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", foreign_keys=[user_id], back_populates="photos")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
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
    user1 = User(id=1, name="lee")
    user2 = User(id=2, name="park")
    photo1 = Photo(id=1, user_id=1, path="aaa.jpg")
    photo2 = Photo(id=2, user_id=2, path="bbb.jpg")
    session.add(user1)
    session.add(user2)
    session.add(photo1)
    session.add(photo2)
    session.commit()

    session.query(Photo).select_from(User).join(User.photos).all()

    assert len(messages) == 1
    assert re.match(
        "SELECT photos.id AS photos_id, photos.path AS photos_path, photos.user_id AS photos_user_id FROM users JOIN photos ON users.id = photos.user_id",
        messages[0],
    )
