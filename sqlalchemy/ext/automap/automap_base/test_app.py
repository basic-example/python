from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.automap import automap_base


def test_case_by_metadata():
    engine = create_engine("sqlite://")
    connect = engine.connect()
    connect.execute("CREATE TABLE users(id int primary key, name varchar(50))")

    metadata = MetaData()
    metadata.reflect(engine)
    Base = automap_base(metadata=metadata)
    Base.prepare()

    assert "id" in dict(Base.classes.users.__table__.columns).keys()
    assert "name" in dict(Base.classes.users.__table__.columns).keys()


def test_case_by_reflect_true():
    engine = create_engine("sqlite://")
    connect = engine.connect()
    connect.execute("CREATE TABLE users(id int primary key, name varchar(50))")

    Base = automap_base()
    Base.prepare(engine, reflect=True)

    assert "id" in dict(Base.classes.users.__table__.columns).keys()
    assert "name" in dict(Base.classes.users.__table__.columns).keys()
