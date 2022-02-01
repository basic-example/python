from sqlalchemy import (Column, Integer, String, create_engine, insert, select,
                        update)
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
    stmt = insert(User.__table__).values(id=1, name="yoo")
    result = connect.execute(stmt)
    stmt = insert(User.__table__).values(id=2, name="kim")
    result = connect.execute(stmt)

    stmt = User.__table__.update().values({"name": "park"})
    result = connect.execute(stmt)
    stmt = select(User.__table__)
    result = connect.execute(stmt)
    assert result.fetchall() == [(1, "park"), (2, "park")]

    stmt = update(User.__table__).values({"name": "yoo"})
    result = connect.execute(stmt)
    stmt = select(User.__table__)
    result = connect.execute(stmt)
    assert result.fetchall() == [(1, "yoo"), (2, "yoo")]

    stmt = update(User.__table__).values(name="lee")
    result = connect.execute(stmt)
    stmt = select(User.__table__)
    result = connect.execute(stmt)
    assert result.fetchall() == [(1, "lee"), (2, "lee")]
