import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.engine import Row
from sqlalchemy.orm import Session, registry

Base = registry().generate_base()


def test_case():
    engine = create_engine("mysql+pymysql://root:1234@localhost/test")
    session = Session(engine)

    assert isinstance(session.get_bind(), sqlalchemy.engine.base.Engine)
    assert isinstance(session.get_bind().url, sqlalchemy.engine.url.URL)
