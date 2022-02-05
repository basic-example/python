from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Bundle, Session, registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def to_string(query):
    return "".join(str(query).splitlines())


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.commit()
    bundle = Bundle("something", User.name)

    for row in session.query(bundle):
        assert row.something.name in ["yoo", "lee"]
