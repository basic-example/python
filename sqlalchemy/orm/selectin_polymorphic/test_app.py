import logging
import re

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, declarative_base, selectin_polymorphic

Base = declarative_base()


class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True)
    type_of = Column(String(50))

    __mapper_args__ = {"polymorphic_on": type_of}


class Nationality(Keyword):
    __tablename__ = "nationalities"
    id = Column(Integer, ForeignKey("keywords.id"), primary_key=True)
    code = Column(String)
    __mapper_args__ = {
        "polymorphic_identity": "nationality",
    }


class Religion(Keyword):
    __tablename__ = "religions"
    id = Column(Integer, ForeignKey("keywords.id"), primary_key=True)
    type = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": "religion",
    }


def test_case():

    engine = create_engine("sqlite://")
    connect = engine.connect()
    session = Session(engine)
    religion = Religion(id=1, type="christian")
    nationality1 = Nationality(id=2, code="US")
    nationality2 = Nationality(id=3, code="KR")
    Base.metadata.create_all(engine)
    session.add(religion)
    session.add(nationality1)
    session.add(nationality2)
    session.commit()
    messages = []

    class StreamHandler(logging.StreamHandler):
        def emit(self, record):
            if re.match("^SELECT", record.msg):
                messages.append(record.msg)

    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.engine").addHandler(StreamHandler())

    result = Query(Keyword).with_session(session).all()

    assert len(result) == 3
    assert isinstance(result[0], Religion)
    assert isinstance(result[1], Nationality)
    assert isinstance(result[2], Nationality)

    assert result[0].type
    assert result[1].code
    assert result[2].code
    assert len(messages) == 4

    messages = []
    result = (
        Query(Keyword)
        .with_session(session)
        .options(selectin_polymorphic(Keyword, [Nationality, Religion]))
        .all()
    )

    assert result[0].type
    assert result[1].code
    assert result[2].code
    assert len(messages) == 3
