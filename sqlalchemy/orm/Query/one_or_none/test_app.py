import pytest
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
    session.add(User(id=2, name="lee", age=20))
    session.add(User(id=3, name="park", age=20))
    session.commit()

    with pytest.raises(Exception) as exception:
        Query(User).with_session(session).one_or_none()

    assert "Multiple rows were found when one or none was required" in str(
        exception.value
    )

    result = Query(User).with_session(session).filter(User.name == "fff").one_or_none()

    assert result == None
