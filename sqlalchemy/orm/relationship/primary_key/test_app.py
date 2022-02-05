from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session, registry, relationship

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


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    user = User(id=1, name="yoo")
    photo1 = Photo(id=1, path="aaa/bbb/ccc.jpg", user_id=1)
    photo2 = Photo(id=2, path="xxx/yyy/zzz.jpg", user_id=1)
    session.add(user)
    session.add(photo1)
    session.add(photo2)
    session.commit()

    assert len(list(user.photos)) == 2
