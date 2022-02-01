from sqlalchemy import (Column, Integer, String, create_engine, delete, insert,
                        select)
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
    stmt = insert(User.__table__).values(id=3, name="lee")
    result = connect.execute(stmt)
    stmt = delete(User.__table__).where(User.__table__.c.id == 1)
    result = connect.execute(stmt)
    stmt = select(User.__table__)
    result = connect.execute(stmt)

    assert result.fetchall() == [(2, "kim"), (3, "lee")]

    stmt = User.__table__.delete().where(User.__table__.c.id == 2)
    result = connect.execute(stmt)
    stmt = select(User.__table__)
    result = connect.execute(stmt)

    assert result.fetchall() == [(3, "lee")]
