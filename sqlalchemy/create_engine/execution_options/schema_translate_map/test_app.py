from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, registry, relationship

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "db1"}
    id = Column(Integer, primary_key=True)
    name = Column(String)
    photos = relationship(lambda: Photo, back_populates="user")


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    path = Column(String)
    user = relationship(lambda: User, foreign_keys=[user_id], back_populates="photos")


def test_case():
    engine = create_engine(
        "sqlite://", execution_options={"schema_translate_map": {None: "db2"}}
    )
    engine.execute("attach database 'test1.db' as db1")
    engine.execute("attach database 'test2.db' as db2")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.query(User).delete()
    session.query(Photo).delete()
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(User(id=3, name="park"))
    session.add(Photo(id=1, user_id=1, path="aaa.jpg"))
    session.add(Photo(id=2, user_id=2, path="bbb.jpg"))
    session.add(Photo(id=3, user_id=3, path="ccc.jpg"))
    session.commit()

    result = Query(User).with_session(session).all()

    assert result[1].photos[0].path == "bbb.jpg"
