from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeferredReflection, declarative_base

Base = declarative_base()


class User(DeferredReflection, Base):
    __tablename__ = "users"


def test_case():
    engine = create_engine("sqlite://")
    connect = engine.connect()
    connect.execute("CREATE TABLE users(id int primary key, name varchar(50))")

    DeferredReflection.prepare(engine)

    assert "id" in dict(User.__table__.columns).keys()
    assert "name" in dict(User.__table__.columns).keys()
