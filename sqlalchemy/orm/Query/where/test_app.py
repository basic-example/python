from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, registry, relationship

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    photos = relationship("Photo")


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    path = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", foreign_keys=[user_id], back_populates="photos")


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.query(User).delete()
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(User(id=3, name="park"))
    session.commit()
    query = Query(User).with_session(session)
    query = query.where(User.name == "lee")
    result = query.all()

    assert len(query._where_criteria) != 0
    assert len(result) == 1
    assert isinstance(result[0], User)
    assert result[0].name == "lee"


def test_case_for_select_in_sub_query():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.query(User).delete()
    session.query(Photo).delete()
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(Photo(id=1, user_id=2, path="aaa.jpg"))
    session.add(Photo(id=2, user_id=2, path="bbb.jpg"))
    session.add(Photo(id=3, user_id=3, path="ccc.jpg"))
    query = session.query(User).where(
        User.id.in_(session.query(Photo).from_self(Photo.user_id))
    )
    result = query.all()

    assert len(query._where_criteria) != 0
    assert len(result) == 1
    assert isinstance(result[0], User)
    assert result[0].name == "lee"
