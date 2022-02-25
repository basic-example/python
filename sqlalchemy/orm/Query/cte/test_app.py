from sqlalchemy import Column, Integer, String, create_engine
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
    session.add(User(id=2, name="lee", age=20))
    session.add(User(id=3, name="park", age=20))
    session.commit()

    Age20User = (Query(User).with_session(session).filter(User.age == 20)).cte()
    result = Query(Age20User).with_session(session).all()

    assert len(result) == 2
    assert result[0].name == "lee"
    assert result[1].name == "park"
