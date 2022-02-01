from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    Text,
    create_engine,
    inspect,
)
from sqlalchemy.orm import declarative_base


def test_case_by_declarative_base():
    Base = declarative_base()

    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        name = Column(String)

    class Post(Base):
        __tablename__ = "posts"
        id = Column(Integer, primary_key=True)
        author_id = Column(Integer)
        subject = Column(String)
        description = Column(Text)

    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    tables = inspect(engine).get_table_names()
    assert len(tables) == 2


def test_case_by_metadata_object():
    metadata = MetaData()

    Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
    )
    Table(
        "posts",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("author_id", Integer),
        Column("subject", String),
        Column("description", Text),
    )

    engine = create_engine("sqlite://")
    metadata.create_all(engine)
    tables = inspect(engine).get_table_names()
    assert len(tables) == 2
