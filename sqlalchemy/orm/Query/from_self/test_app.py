from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Query, Session, registry

Base = registry().generate_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)


def test_case():
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    session = Session(engine)
    session.add(User(id=1, name="yoo"))
    session.add(User(id=2, name="lee"))
    session.add(User(id=3, name="park"))
    session.commit()
    result = (
        Query(User)
        .with_session(session)
        .filter(User.name == "lee")
        .from_self(User.name)
        .first()
    )

    assert len(result) == 1
    assert result[0] == "lee"
