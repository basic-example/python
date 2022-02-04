from sqlalchemy import Table, create_engine
from sqlalchemy.orm import registry

Base = registry().generate_base()


def test_case():
    engine = create_engine("sqlite://")
    connect = engine.connect()
    connect.execute("CREATE TABLE users(id int primary key, name varchar(50))")

    class User(Base):
        __table__ = Table("users", Base.metadata, autoload_with=engine)

    assert "id" in dict(User.__table__.columns).keys()
    assert "name" in dict(User.__table__.columns).keys()
