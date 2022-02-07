from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.engine import Row, RowMapping
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
    row = result.first()

    assert isinstance(row, Row)
    assert isinstance(row._fields, tuple)
    assert isinstance(row._asdict(), dict)
    assert len(row._fields) == 1
    assert row._fields[0] == "User"
    assert len(row._asdict()) == 1
    assert "User" in row._asdict()
    assert isinstance(row._asdict()["User"], User)
    assert row._asdict()["User"] == row[0]
    assert isinstance(row._mapping, RowMapping)
