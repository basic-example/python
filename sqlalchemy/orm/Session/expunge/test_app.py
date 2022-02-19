from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def test_case():
    engine = create_engine("sqlite://", echo=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(User(id=1, name="yoo", age=10))
    session.add(User(id=2, name="lee", age=20))
    session.add(User(id=3, name="park", age=30))
    session.commit()
    query = Query(User).with_session(session)
    result = query.all()

    result[0].name = "yoon"
    result[1].name = "kim"
    session.commit()
    result = query.all()

    assert result[0].name == "yoon"
    assert result[1].name == "kim"

    result[0].name = "kang"
    result[1].name = "jung"
    session.expunge_all()
    session.commit()
    result = query.all()

    assert result[0].name == "yoon"
    assert result[1].name == "kim"
