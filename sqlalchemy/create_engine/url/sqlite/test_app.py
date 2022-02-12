from sqlalchemy import Column, Integer, String, create_engine, inspect, select
from sqlalchemy.orm import registry


@registry().mapped
class User:
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_case():
    engine = create_engine("sqlite://")
    connect = engine.connect()
    User.__table__.create(engine)
    stmt = User.__table__.insert().values(id=1, name="yoo")
    result = connect.execute(stmt)
    stmt = select(User.__table__)
    result = connect.execute(stmt)

    assert result.fetchall() == [(1, "yoo")]
