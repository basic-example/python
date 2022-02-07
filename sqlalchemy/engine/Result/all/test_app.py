from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session, registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(User(id=3, name="park"))
    session.commit()
    query = select(User)
    result = session.execute(query)
    data = result.all()

    assert len(data) == 3
    assert isinstance(data, list)
    assert isinstance(data[0], Row)
    assert len(result.all()) == 0
