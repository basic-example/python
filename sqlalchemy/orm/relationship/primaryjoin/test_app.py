from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, registry, relationship

Base = registry().generate_base()


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    path = Column(String)
    user = relationship(
        "User", primaryjoin="Photo.user_id == User.id", back_populates="photos"
    )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    photos = relationship(
        "Photo", primaryjoin="Photo.user_id == User.id", back_populates="user"
    )


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)

    user1 = User(id=1, name="yoo")
    user2 = User(id=2, name="lee")
    photo1 = Photo(id=1, user_id=1, path="aaa/bbb/ccc.jpg")
    photo2 = Photo(id=2, user_id=1, path="xxx/yyy/zzz.jpg")
    photo3 = Photo(id=3, user_id=2, path="xxx/yyy/zzz.jpg")

    session.add(user1)
    session.add(user2)
    session.add(photo1)
    session.add(photo2)
    session.add(photo3)
    session.commit()

    assert len(user1.photos) == 2
    assert len(user2.photos) == 1
