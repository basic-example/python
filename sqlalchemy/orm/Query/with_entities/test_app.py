import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, func
from sqlalchemy.orm import Query, Session, registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(User(id=1, name="yoo", age=10))
    session.add(User(id=3, name="lee", age=20))
    session.add(User(id=4, name="park", age=30))
    session.commit()
    query = Query(User).with_session(session)

    result = query.first()
    assert hasattr(result, "name")
    assert hasattr(result, "age")
    assert hasattr(result, "id")

    result = query.with_entities(User.name).first()
    assert hasattr(result, "name")
    assert not hasattr(result, "age")
    assert not hasattr(result, "id")

    result = query.with_entities(func.max(User.age)).first()
    assert type(result) == sqlalchemy.engine.row.Row
    assert tuple(result) == (30,)

    result = query.with_entities(func.max(User.age)).scalar()
    assert type(result) == int
    assert result == 30
