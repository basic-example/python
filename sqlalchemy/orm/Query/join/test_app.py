from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine,
                        select)
from sqlalchemy.orm import Query, Session, registry, relationship

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
    session.query(User).delete()
    session.query(Photo).delete()
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(User(id=3, name="park"))
    session.add(Photo(id=3, user_id=2, path="aaa.jpg"))
    session.add(Photo(id=4, user_id=2, path="bbb.jpg"))
    session.add(Photo(id=5, user_id=3, path="ccc.jpg"))
    session.commit()

    query = Query(User).with_session(session)
    query = query.filter_by(name="lee")
    query = query.join(Photo)
    result = query.all()

    assert len(result) == 1

    query = select(User)
    query = query.filter_by(name="lee")
    query = query.join(Photo)
    result = session.execute(query).all()

    assert len(result) == 2
