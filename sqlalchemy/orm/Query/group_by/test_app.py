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
    session.add(User(id=3, name="lee"))
    session.add(User(id=4, name="park"))
    session.commit()
    query = Query(User).with_session(session)
    data = query.filter_by(name="lee").group_by(User.name).all()

    assert len(data) == 1
    assert isinstance(data[0], User)
    assert data[0].name == "lee"
